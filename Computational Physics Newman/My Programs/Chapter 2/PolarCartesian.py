# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:43:03 2015

@author: Kike
"""

from math import sin, cos, pi, sqrt, atan

print("We are going to convert cartesian coordinates into polar ones.")
x = float(input("Please, enter the value of the x coordinate: "))
y = float(input("Please, enter the value of the y coordinate: "))

r = sqrt(x**2 + y**2)
theta_rad = atan(y/x)

theta_deg = theta_rad * 180 / pi

print("The polar coordinates of the point are (", r,", ", theta_deg, ").", sep="")