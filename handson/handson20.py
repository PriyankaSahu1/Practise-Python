#handson 20

n=int(input("Enter the no of terms: "))
a=0 
b=1
if n<=0:
  print("please enter positive numbers")
elif n==1:
  print("Fibonacci series:",a)
elif n==2:
  print(a)
  print(b)
else:
  print(a)
  print(b)
  while(n>2):
    temp=a+b
    print(temp)
    a=b
    b=temp
    n=n-1
