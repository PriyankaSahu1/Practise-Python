#handson 16

#prime number or not
num = int(input("Enter a number: "))

if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")

#prime number in a specified range
n = int(input("Enter a number: "))
print("prime numbers are:")
for num in range(1,n):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
