# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:41:07 2015

@author: Kike
"""

# A simple example on recursions: calculating the factorial.

def factorial2(n):
    if n == 0:
        return 1
    else:
        return n*factorial2(n-1)
        
print(factorial2(6))