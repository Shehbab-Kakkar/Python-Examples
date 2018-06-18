#!/usr/bin/env python3.6
def add(a, b):
     return( a + b )
print("second  Add function  ",add(2,3))
print(__name__)

def sub(c,d):
      return( c - d )

if __name__ == "__main__":     
    print("second Sub function  ",sub(3,2))

print(__name__)   

#If the same python script is executed then the __name__ variable 
# is set as __name__
