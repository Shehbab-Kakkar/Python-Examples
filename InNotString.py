#!/usr/bin/env python3.6
s=input('Enter some string: ')
subs=input('Enter Substring to search: ')
if subs in s:
    print(" '%s' found in Main String" % subs)
else:
    print("'{}' not found in Main String".format(subs))







