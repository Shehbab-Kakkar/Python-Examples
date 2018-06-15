#!/usr/bin/python3.6
a=int(input("Enter  First Number:"))
b=int(input("Enter  Second Number:"))
c=int(input("Enter  Third Number:"))
max=a if a>b and a>c else b if b>c else c
print("Max Value",max)



