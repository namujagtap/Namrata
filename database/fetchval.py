#write a program fetch values from value from table
import MySQLdb

try:
    query="create table stdinfo(name varchar(50),birthplace varchar(20),address varchar(40))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="select*from stdinfo"
    cur.execute(query)
    print("excecute excecute")
    #mycon.commit()
    tdata=cur.fetchall()
    print("Records from table")
    for row in tdata:
        print("name : ",row[0])
        print("birthplace : ",row[1])
        print("address : ",row[2])
except:
    print("value not fetch from table...")
finally:
    cur.close()
    print("cursor connection close...")
    mycon.close()
    print("DB connection close...")