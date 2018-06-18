#!/usr/bin/env python3.6
#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#https://www.youtube.com/watch?v=cVzOEli3zaA
#https://www.youtube.com/watch?v=dLgGSe1N4gA
from secondModule import add #from second module import function add
from secondModule import sub  
print("main Add function:  ",add(2,2))
print(__name__)
print("main Sub function:  ",sub(4,2))
print(__name__)


#import secondModule as s
#print("main Add function:  ",s.add(2,2))

