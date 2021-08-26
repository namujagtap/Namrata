#with open("text.txt","w",encoding="utf-8")as f:
#    f.write("hello \n how are you")

#Writing in file
f = open("text.txt", "w")
f.write("agar tum saat ho")
f.close()
f = open("text.txt", "r")
print(f.read())
#Writing in file 
with open("text.txt", "w",encoding='utf-8')as f:
    f.write("my rulesmy attitude thats my life")
    f.close()
    f = open("text.txt", "r")
print(f.read())
##Reading file
f = open('text.txt','r',encoding='utf-8')
print(f.read())
# closing opened file
f = open("text.txt", "r")
f = open("text.txt", "r",encoding='utf-8')
print(f.read())
f.close()