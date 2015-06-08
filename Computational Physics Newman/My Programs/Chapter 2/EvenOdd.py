# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:48:41 2015

@author: Kike
"""

print("Enter two integers, one even, and the other odd.")
m = int(input("Please enter now the first integer: "))
n = int(input("Please enter now the second integer: "))
while (m + n) % 2 == 0:
    print("One has to be even, and the other odd!")
    m = int(input("Please enter again one integer: "))
    n = int(input("And now the other one: "))
print ("Well done! You chose numbers", m, "and", n)