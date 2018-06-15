#!/usr/bin/env python3.6
#progam to find biggest of three numbers from the keyboard
n1=eval(input("Enter first number: "))
n2=eval(input("Enter Second number: "))
n3=eval(input("Enter Third number: "))
if n1>n2 and n1>n3:
    print("Bigger number is",n1)
elif n2>n3:
    print("Bigger number is",n2)
else:
    print("Bigger number is",n3)
