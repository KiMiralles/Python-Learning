# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:40:46 2015

@author: Kike
"""
from math import sqrt, pi

v1 = float(input("Please enter the velocity at Perihelium [m/s]: "))
l1 = float(input("Please enter the distance to the Sun at Perihelium [m]: "))

G = 6.6738e-11
M = 1.9891e+30
GM = G*M

v2 = GM/(l1*v1) - sqrt(GM**2/(l1*v1)**2 + v1**2 - 2*GM / l1)
print(v2)
l2 = l1*v1/v2
print(l2)

T_sec = pi*(l1+l2)*sqrt(l1*l2) / (l1*v1)
T_years = T_sec / (60*60*24*365.25)
exc = (l2 - l1) / (l2 + l1)

print("The velocity at Aphelion is", v2, "m/s.")
print("The distance at Aphelion is", l2, "m/s.")
print("The period of the orbit is", T_years, "years.")
print("The excentricity of the orbit is", exc)