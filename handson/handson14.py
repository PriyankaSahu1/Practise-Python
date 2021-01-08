#handson 14

list1=[1,2,3,4,5,6,7,8,9,10]
list2=["raj","lilly","riya","pia","ridhi","sidhi","akhil","sandy","anup","arup"]

#printing all names
print(list2)

#Read the index from the  user and print the corresponding name from both list
print("enter any index value from 0-9")
x=int(input('enter integer value for x:'))
print(list1[x],"",list2[x])

#Print the names from 4th position to 9th position
for i in  range(4,9):
    print(list2[i])

#Print all names from 3rd position till end of the list
for i in  range(3,10):
    print(list2[i])

#Concatenate two lists and print the output
print(list1+list2)

#Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
for i in  range(10):
    print(list1[i],"",list2[i])

#Repeat list elements by specified number of times (N- times, where N is entered by user)
n=int(input('enter integer value for n:'))
for i in  range(n):
    print(list1+list2)

