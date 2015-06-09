# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:30:15 2015

@author: Kike
"""

from numpy import array

a = array([1,2,3,4], int)
b = array([2,4,6,8], int)

print(b/a+1) # This should give an array [3 3 3 3].

print(b/(a+1)) # This would lead to an integer array --> float array change, with
               # the following result [1 1.333... 1.5 1.6]

print(1/a) # This last one will give [1 0.5 0.333... 0.25]