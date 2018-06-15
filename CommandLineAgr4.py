#!/usr/bin/env python3.6
#
#
#Read a group of int values from the keyboard as cmd line arg and print sum
from sys import argv
args=argv[1:]
sum=0
for x in args:
  n=eval(x)
  sum +=n 
print("The sum:",sum)
