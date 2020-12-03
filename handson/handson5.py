# handson 5

import sys

if len(sys.argv)>0:

    print(sys.argv)

else:
    print("enter more arguments")

a=0

for i in sys.argv:
    if i.isdigit() == True:
        b=int(i)
        if a<b:
            a=b

print(a)
        
