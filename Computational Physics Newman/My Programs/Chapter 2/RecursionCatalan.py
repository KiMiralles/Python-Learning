# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:44:01 2015

@author: Kike
"""

def Catalan(n):
    if n == 0:
        return 1
    else:
        return ((4*n - 2)/(n+1))*Catalan(n-1)

print(Catalan(100))