# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:52:07 2015

@author: Kike
"""

print("""We are going to calculate all numbers in the Fibonacci sequence
up until the number you pick.""")
limit = int(input("Please enter the upper bound to the calculation: "))

# Here's how to do it in a traditional way.

f1 = 1
f2 = 1

while f1 < limit:
    fsum = f1 + f2
    f1 = f2
    f2 = fsum
    print(fsum)

# Here's how to do it, taking advantage of Python's multiple assignment.

f1, f2 = 1, 1

while f1 < limit:
    print(f1)
    f1, f2 = f2, f1+f2
    
# As a side note here: python fully evaluates the right hand side before
# assigning anything on the left side. So the values of f2, f1+f2 are
# calculated BEFORE changing the actual values of f1 and f2.