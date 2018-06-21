#!/usr/bin/env python3.6
a,b = 2,3
c,d = "Sea","Ocean"
print(id(a),"-",type(a), "- Value of a = {0} and b = {1} ".format(a,b),end=":")
print("A is ",a,end=" >>>>>")
print("C and D together are ",c+d)

print("\n\n")
hello = "Shehbab"
world = "kakkar"

print(hello + " " + world)
print("%s %s" % (hello, world))
print("{} {}".format(hello, world))
print(' '.join([hello, world]))
