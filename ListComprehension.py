#!/usr/bin/env python3.6
#for num in range(x)
#   num = int(input())
#https://stackoverflow.com/questions/16129650/what-does-x-2-0-mean
#https://www.programiz.com/python-programming/list-comprehension

"""
value=int(input("Enter the number: "))
if value % 2  == True:
   print("%d Number is True" % value)
elif value % 2 == False:
   print("%d Number is False" % value)
"""
for x in range(1,10):
     if x % 2 == True:
        print(x)
     else:
        print(x * 100)
print([x if x % 2 else x * 100 for x in range(1, 10) ])
print(1 % 2)
print(2 % 2)
