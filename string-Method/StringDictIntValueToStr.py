#!/usr/bin/env python3.6
#https://stackoverflow.com/questions/44619572/join-the-values-only-in-a-python-dictionary
diction={"Name":"Shehbab", "Age": 27}
#print(''.join(diction),"\n",''.join(diction.values())) 
#print(''.join(diction))
#rint(''.join(str(diction.values())))

print(''.join(map(str, diction.values())))


