#!/usr/bin/env python3

l = list(range(0,255))
newL = []

def invert(l):
   c = 0 
   for num in l:
      l[c] = str(255 - int(num))
      c+=1

def inverted(l):
    newL = []
    c = 0 
    for num in l:
       newL.append(str(255-int(num)))
       c+=1

    return newL
