#!/usr/bin/python3.6
MyList = [[1,2,3,4],
          [5,6,7,8],   
          [9,10,11,12]]

for x in zip(*MyList):
    print(x)

"""
Output: 
(1, 5, 9)
(2, 6, 10)
(3, 7, 11)
(4, 8, 12)

"""
