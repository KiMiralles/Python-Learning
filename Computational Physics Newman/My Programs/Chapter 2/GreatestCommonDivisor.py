# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:47:32 2015

@author: Kike
"""

def GCD(m,n):
    if n == 0:
        return m
    else:
        return GCD(n, m % n)

# print(GCD(108, 192))
# Notice that it does not care about the order in which you choose the integers!