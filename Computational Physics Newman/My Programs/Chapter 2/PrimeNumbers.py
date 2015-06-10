# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:30:01 2015

@author: Kike
"""
from math import sqrt

while True:

    n = int(input("We are going to find all prime numbers up to a certain number >=2. Which number would you like? "))

    if n < 2:
        print()
        print("The number must be >=2. Restarting the program...")
        print()
    else:
        break

primes = [2]

for each in range(3, n+1):
    for i in range(2, 1+int(sqrt(each))):
        if each % i == 0:
            break
    else:
        primes.append(each)

print(primes)
#print(len(primes))