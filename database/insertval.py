#write a program to insert values in table
import MySQLdb

try:
    query="create table stdinfo(name varchar(50),birthplace varchar(20),address varchar(40))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="insert into stdinfo values('Namrata','solapur','solapur city') "
    query="insert into stdinfo values('surya','pune','goa')"
    cur.execute(query)
    print("excecute excecute")
    mycon.commit()
    print(query+"sucessfully fired.....")
except:
    print("table not created...")
finally:
    cur.close()
    print("cursor connection close...")
    mycon.close()
    print("DB connection close...")