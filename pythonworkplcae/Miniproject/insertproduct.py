import MySQLdb

try:
    query="create table cosmaticproduct(name varchar(50),price int(20))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="product")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="insert into cosmaticproduct values('lipstick','400') "
    query="insert into cosmaticproduct values('nailpaint','50','khushi')"
    query="insert into cosmaticproduct values('makupfixer','500') "
    query="insert into cosmaticproduct values('perfume','600') "
    query="insert into cosmaticproduct values('fondation','400')"
    query="insert into cosmaticproduct values('maskara','180')"
    query="insert into cosmaticproduct values('primer','150')"
    query="insert into cosmaticproduct values('consiler','250')"
    query="insert into cosmaticproduct values('eyeshadow','500')"
    query="insert into cosmaticproduct values('eyeliner','150')"    
    cur.execute(query)
    print("excecute excecute")
    mycon.commit()
    print(query+" value inserted sucessfully .....")
except:
    print("value not inserted...")
finally:
    cur.close()
    print("cursor connection close...")
    mycon.close()
    print("DB connection close...")