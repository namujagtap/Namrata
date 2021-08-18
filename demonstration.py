#if
S=50
n=int(input("enter number"))
if S>n:
    print(S,": is greater than user input:",n)
else:
    print(S,": is less than user input:",n)     

#elif
if n>0:
    print("positive number")
elif n==0:
    print("user enter zero")
else:
    print("negative number")

#for loop
numbers=[1,2,3,4,5,6,7,8,9]
sum=0
for num in numbers:
    sum=sum+num
    print("sum :",sum)
#range
print("range seque:",range(10))
print("range seque all items :",list(range(10)))
print("range with 2 args",range(2,24,3))

for num in range(0,10):

    print("num :",num)
#while loop
s=0
i=1

while i<=n:
    s=s+i
    i=i+1
print("sum=",sum)
# break continue pass

if 10>7:
    pass
for b in "good afternoon":
    if b=='f':
        break
    print(b)

#continue
if 10>7:
    pass
for b in "good afternoon":
    if b=='e':
        continue
    print(b)