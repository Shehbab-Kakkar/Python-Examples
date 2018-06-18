#!/usr/bin/env python3.6
#https://stackoverflow.com/questions/1419046/python-normal-arguments-vs-keyword-arguments


def get_data(engine, *queries, **properties):
    print(engine,queries,properties)

get_data('google', 'python', 'flask', 'django', limit = 10, verbose = True)

"""
Output: google ('python', 'flask', 'django') {'limit': 10, 'verbose': True}
       normal      tuples                     dictitionary

"""

