#handson 19
#a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
   # i) Break the loop if the value is 50
    #ii) Use continue for the values 10,20,30,40,50

for i in range (1,101):
    if i%2!=0:
       continue
    if(i==50):
        break
    if i ==10 or i==20 or i==30 or i==40 or i==50:
        continue
    print(i)



#b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
 #     i) Break the loop if the value is 90
  #    ii) Use continue for the values 60,70,80,90

j=1
while j<=100:
     if j%2!=0:
        continue
     if(j==90):
        break
     if j ==60 or j==70 or j==80 or j==90:
        continue
     print(j)
     j=j+1
