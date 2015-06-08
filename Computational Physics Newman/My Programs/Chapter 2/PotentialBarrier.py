# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:46:37 2015

@author: Kike
"""

from math import sqrt

E = float(input("Enter the initial energy of the particle in eV: "))
V = float(input("Enter the magnitude of the potential barrier in eV: "))

hbar = 6.58e-16
m = 9.11e-31

k1 = sqrt(2*m*E) / hbar
k2 = sqrt(2*m*(E-V)) / hbar

R = ((k1 - k2) / (k1 + k2))**2
T = (4*k1*k2) / (k1+k2)**2

print("The probability of reflection is ", R, ".", sep="")
print("The probability of transmission is ", T, ".", sep="")