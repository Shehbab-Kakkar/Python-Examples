#!/usr/bin/env python3.6
def factorial2(n):
    k = 1
    for i in range(1,n+1):
      k *= i
      yield k    
f=factorial2(5)
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

"""
<class 'generator'>
1
2
6
24
120
"""
