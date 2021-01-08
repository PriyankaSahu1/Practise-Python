#handson 15

list=["abc","bcd","jkl","xyz","mno"]

#using membership operator
if("abc" in list):
    print("abc is available")
else:
    print("abc is not present")

#without using membership operator
for i in range(5):
    if(list[i]=="abc"):
        print("available")
        break
    else:
        print("not available")

#printing list in reverse direction

list.reverse()
print(list)
