#handson 18
list=[]
#using for loop
for i in range(1,101):
    list.append(i)

print("elemets from 1-100",list)
list.reverse()
print("elements from 100-1",list)

#using while loop

print("while")
listA=[]
j=1
while (j<=100):
    listA.append(j)
    j+=1

print("elemets from 1-100",listA)
listA.reverse()
print("elements from 100-1",listA) 

#mystring
mystring="Hello World"

for k in mystring:
    print(k)
