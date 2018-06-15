#!/usr/bin/env python3.6
num=int(input("Enter the number of rows"))
for i in range(1,num+1):
    for j in range(1,i+1):
          print("*",end=":>")
    print() ##To move to the next line

"""
  First pass:
num=5
  i=1,4  mean-1
j 1,2   mean -1 time 

*

i=2,   mean=2
j=1,3  mean=2

* * 

i3
i=1,4 mean 3 time

* * * 

##################
Enter the number of rows 5
*:>
*:>*:>
*:>*:>*:>
*:>*:>*:>*:>
*:>*:>*:>*:>*:>
==========


"""
