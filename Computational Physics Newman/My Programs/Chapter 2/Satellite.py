# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:21:01 2015

@author: Kike
"""

T = float(input("Insert the value of the orbital period [seconds]: "))

G = 6.67e-11
M = 5.97e+24
R = 6371e+3
pi2 = 3.141592**2

h = (G*M*(T**2)/(4*pi2))**(1/3) - R
print ("The height of the orbit is", h, "meters above Earth's surface.")