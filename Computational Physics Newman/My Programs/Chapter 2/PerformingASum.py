# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:29:41 2015

@author: Kike
"""
from numpy import loadtxt, sum

# First, perform a traditional sum.

suma = 0

for k in range(1, 101):
    suma += 1/k
print(suma)

# Now, make the sum of the squares of the values of a given file...

# ...using an array operation.

suma2 = sum((loadtxt("Values2.txt", float))**2)
print(suma2)

# ...using a for loop.

suma3 = 0
values = loadtxt("Values2.txt", float)

for each in values:
    suma3 += each**2
print(suma3)