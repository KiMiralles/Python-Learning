# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:16:16 2015

@author: Kike
"""

h = float(input("Enter the height of the tower [in meters]: "))
t = float(input("Enter the desired time interval [in seconds]: "))
g = 9.81

y = 0.5*g*t**2

print("The ball is at a height of", h-y, "meters")