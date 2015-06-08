# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:01:06 2015

@author: Kike
"""

print("""We are going to print out all the Catalan numbers up until
 a number you pick.""")
limit = int(input("Enter the upper bound, please: "))

Cn = 1
n = 0

while Cn < limit:
    print(Cn)
    n += 1
    Cn_plus = int((Cn * (4*n + 2)) / (n + 2))
    Cn = Cn_plus