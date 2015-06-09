# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:40:17 2015

@author: Kike
"""

from math import sqrt

L = 100
M = 0

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if i == 0 and j == 0 and k == 0:
                continue
            else:
                M += ((-1)**(i+j+k)) * 1/(sqrt((i**2)+(j**2)+(k**2)))

print("For L=", L, "the Madelung constant M is", M)