#!/usr/bin/env python3.6
#https://stackoverflow.com/questions/1419046/python-normal-arguments-vs-keyword-arguments

#farg / formal agruments
def add(a,b):
    sum = a + b
    return sum
print("Can't handle multiple agruments",add(2,3))
#Output: Can't handle multiple agruments 5


# *args / Variable number of non keyworded agruments
def add(*nums):
    return sum(nums)
    #return nums[2]
print("Multiple agruments: ",add(2,3,4,5))

#Output: Multiple agruments:  14

# **kwargs / Variable number of keyworded agruments
def record(**data):
    print(data)
record(name= "Nikhil", rollno = 85, age = 20)

#Here we will get dictitionary of data
#Output: {'name': 'Nikhil', 'rollno': 85, 'age': 20}



