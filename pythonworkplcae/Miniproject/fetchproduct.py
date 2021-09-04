import MySQLdb

try:
    query="create table cosmaticproduct(name varchar(50),price int(20))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="product")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="select*from cosmaticproduct"
    cur.execute(query)
    print("excecute excecute")
    #mycon.commit()
    tdata=cur.fetchall()
    print("Records from table")
    for row in tdata:
        print("name : ",row[0])
        print("price : ",row[1])
except:
    print("value not fetch from table...")
finally:
    cur.close()
    print("cursor connection close...")
    mycon.close()
    print("DB connection close...")