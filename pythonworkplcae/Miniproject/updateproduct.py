import MySQLdb

try:
    query="create table cosmaticproduct(name varchar(50),price int(20))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="product")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="update cosmaticproduct set brand='lakme'where name='primer'"
    query="update cosmaticproduct set brand='fogg'where name='perfume'"
    query="update cosmaticproduct set brand='hudabeauty'where name='makupfixer'"
    query="update cosmaticproduct set brand='matte'where name='lipstick'"
    query="update cosmaticproduct set brand='maybellile'where name='fondation'"
    query="update cosmaticproduct set brand='amabr'where name='maskara'"
    query="update cosmaticproduct set brand='blueheaven'where name='consiler'"
    query="update cosmaticproduct set brand='glittr'where name='eyeshadow'"
    query="update cosmaticproduct set brand='nykaa'where name='eyeliner'"
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