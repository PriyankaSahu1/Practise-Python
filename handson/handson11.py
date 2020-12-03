#handson11
#Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.

x=int(input('enter x:'))
y=int(input('enter y:'))

# & Binary AND
c=x & y
print('AND:',c)

#| Binary OR
c=x|y
print('OR:',c)

#^ Binary XOR
c=x^y
print('xor:',c)

#~ Binary Ones Complement
c=~x
print('~ Binary Ones Complement:',c)

#<< Binary Left Shift
c = x << 2;
print('left shift:',c)

#>> Binary Right Shift
c=x >>2
print('right shift:',c)


