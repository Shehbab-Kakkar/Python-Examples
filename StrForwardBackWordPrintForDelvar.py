#!/usr/bin/env python3.6
s=input('Enter some string: ')
n=len(s)
print("Length of string is {}".format(n)) 
print("Length of string is %s :::" % n) 
print()
print("Data N Forward Direction")

i=0
while i<n:
  print(s[i],end=" ")
  i+=1

print("i=",i)
print()

print("Data N Backward Direction")
i=n-1
while i>=0:
  print(s[i],end="  ")
  i-=1
print("i=",i)

#del i 
#print(i)
#pass 

print("String reverse with negative index")
i=-1
while i>=(-n):   #-1>-2
  print(s[i],end="  ")
  i-=1
print("i=",i)


