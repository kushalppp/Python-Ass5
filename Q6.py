#!/usr/bin/python3

from functools import *
l=[1,2,3,4,5,6,7,8,9,10]
x=reduce(lambda x,y:x+y,l)
print(x)

Output:-
55
