#!/usr/bin/python3

def strlen(x,y):
 z=len(x)
 q=len(y)
 if z<q:
  print(y,"is maxlen",q)
 elif z>q:
  print(x,"is maxlen",z)
 elif z==q:
  print(x)
  print(y)

s1=str(input("enter string1:-"))
s2=str(input("enter string2:-"))
strlen(s1,s2)

Output:-
enter string1:-namrata
enter string2:-guru
namrata is maxlen 7