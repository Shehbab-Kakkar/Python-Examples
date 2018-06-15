"""
*
***
*****
Enter the number of rows 3
( 1 , 1 ) 
( 2 , 1 ) ( 2 , 2 ) ( 2 , 3 ) 
( 3 , 1 ) ( 3 , 2 ) ( 3 , 3 ) ( 3 , 4 ) ( 3 , 5 )
"""
#!/usr/bin/env python3.6
num=int(input("Enter the number of rows"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
          print("(",i,",",j,")",end=" ")
    k=k+2      
i    print() ##To move to the next line
