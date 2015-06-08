# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:43:03 2015

@author: Kike
"""

from math import sin, cos, pi

print("We are going to convert polar coordinates into cartesian ones.")
r = float(input("Please, enter the value of the radial coordinate: "))
theta_deg = float(input("""Please, enter now the value of the angular
coordinate [in degrees]: """))

theta_rad = theta_deg * pi / 180

x = r * cos(theta_rad)
y = r * sin(theta_rad)

print("The cartesian coordinates of the point are (", x,", ", y, ").", sep="")