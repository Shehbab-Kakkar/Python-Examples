#!/usr/bin/python3.6 
from sys import argv
print("The number of command line agruments: ",len(argv))
print("The list of command line arguments",argv)
print("Command line arguments one by one")
for x in argv:
    print(x)
print("Slice Operator result:",argv[1:3])
