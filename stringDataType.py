
#!/usr/bin/env python3.6
s=input("Enter some String:")
i=0
for x in s:
  print("The character present at positive index {} and at negative index:{} is :{}".format(i,i-len(s),x))
  i+=1

"""
Enter some String: durga
The character present at positive index 0 and at negative index:-5 is :d
The character present at positive index 1 and at negative index:-4 is :u
The character present at positive index 2 and at negative index:-3 is :r
The character present at positive index 3 and at negative index:-2 is :g
The character present at positive index 4 and at negative index:-1 is :a
"""
