#!/usr/bin/python3.6
name = ['Bob','Tom','Sandy','Mohit']
age = [19,29,33]
grade = ['A','B','C','D']

for x in zip(name,age,grade):
      print(x)

"""
('Bob', 19, 'A')
('Tom', 29, 'B')
('Sandy', 33, 'C')
"""
