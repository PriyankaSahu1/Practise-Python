#handson12
#Read 10 numbers from user and find the average of all.
#a) Use comparison operator to check how many numbers are less than average and print them
#b) Check how many numbers are more than average.
#c) How many are equal to average.

a=[1]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
print(a)

sum=sum(a)
avg=sum/len(a)
print(avg)
