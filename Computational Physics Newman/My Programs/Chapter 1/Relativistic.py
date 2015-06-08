# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:29:28 2015

@author: Kike
"""

from math import sqrt

Ax = float(input("Specify the distance between planets in light-years: "))
beta = float(input("Specify the velocity as a fraction of c: "))

At_seconds_earth = 10 * 365.25 * 24 * 60 * 60 / beta
At_years_earth = At_seconds_earth / (60 * 60 * 24 * 365.25)

print("From Earth, it takes the spaceship", At_years_earth, "years to reach the planet.")

gamma = 1 / sqrt(1 - beta**2)

At_seconds_spaceship = gamma * (At_seconds_earth - beta * 10 * 365.25 * 24 * 60 * 60)
At_years_spaceship = At_seconds_spaceship / (60 * 60 * 24 * 365.25)

print("However, from the spaceship, it takes only", At_years_spaceship, "years to reach the planet.")
