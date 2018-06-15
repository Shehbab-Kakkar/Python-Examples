#!/usr/bin/env python3.6
s=input("Enter some string: ")
i=0
for x in s:
  if i!=0:
    print("The character present at",i,"is",x)
    i=i+1
print("hello")
################range
for y in range(6):
    print("hello")

for y in range(4):
    if y%2!=0:
        print(y)

for x in range(1,10,2):
      print(x)
print("\n\n")
for x in range(11,1,-2):
      print(x)
############################

list=eval(input("Enter some list"))
sum=0
for x in list:
    sum=sum+x
print("The sum:",sum)

#Output:-
#Enter some list [10,20,30]
#The sum: 60
#############################
