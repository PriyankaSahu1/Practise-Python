#handson 2
#Write a program to find the biggest of 3 numbers (Use If Condition)

x=int(input('enter x:'))
y=int(input('enter y:'))
z=int(input('enter z:'))

if(x>y) and (x>z):
    print('biggest:',x)
elif(y>x) and (y>z):
  print('biggest:',y)
else:
  print('biggest:',z)
