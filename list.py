x = [1,2,3,4,5,6,7,8,9,0]
print("x=",x)
print("list x =",x[2:5])
print("list x =",x[1:9])
print("list x =",x)
print("list x =",x[7])
print("list x =",x[3:5])
print("list x =",x[2])
print("list x =",x[5])
print("list x =",x[6:9])
print("list x =",x[4])
#extract index number 2 to 5
print("list x",x[2:5])
#print list element reverse
print("list x reverse:",x[::-2])
#using append ,insert add element in list
x.append(12)
print("\n after add 12 value in list=",x)
x.insert(3,'hello')
print("\n insert 3 in list=",x)
#using pop,remove,del remove element 
x.pop(7)
print("\n list after pop x[7]=",x)
x.remove(2)
print("\n list after revome x[2]=",x)
del(x[4])
print("\n list after del x[4]",x)
x.clear()
print("\n list after clear",x)