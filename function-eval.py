#!/usr/bin/env python3.6
x=eval(input("Enter the number:> "))
print(type(x))
for x1 in x:
    print(x1)
"""
Result of the Program

[root@centos7 Python]# ./function1.py
Enter the number:> 10.5
<class 'float'>
[root@centos7 Python]# ./function1.py
Enter the number:> 10,20,40
<class 'tuple'>
[root@centos7 Python]# ./function1.py
Enter the number:> [10,20,40]
<class 'list'>

[root@centos7 Python]# ./function1.py
Enter the number:> False
<class 'bool'>

"""
