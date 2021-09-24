#!/usr/bin/python3


def seprtr(x):
 x=int(x)
 t1=x
 return t1 
total=0
x=input("enter no in one line:-")
l=x.split(",")
for y in l:
 t1=seprtr(y)
 total=total+t1
print("total",total)

Output:-
enter no in one line:-1,5,64,8,6,4
total 88
