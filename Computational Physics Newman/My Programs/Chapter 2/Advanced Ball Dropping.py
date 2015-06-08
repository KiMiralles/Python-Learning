# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:10:44 2015

@author: Kike
"""
g = 9.81
h = float(input("""We are going to calculate the time it takes a ball
to reach the ground when dropped from a tower of height h.
Please, insert the height of the tower in meters: """))

t = (2 * h / g)**0.5

print("The ball reaches the ground after", t, "seconds.")