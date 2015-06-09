# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:57:34 2015

@author: Kike
"""

a1, a2, a3, a4 = 15.67, 17.23, 0.75, 93.2

#Z = int(input("Please enter the value of Z: "))

optimum_bindings = []

for Z in range(1, 101):

    B_pernucleon_optimum = 0
    A_optimum = 0

    for A in range(Z, 3*Z+1):

        if A % 2 != 0:
            a5 = 0.0
        elif A % 2 == 0 and Z % 2 == 0:
            a5 = 12.0
        elif A % 2 == 0 and Z % 2 != 0:
            a5 = -12.0

        B = a1*A - a2*(A**(2/3)) -a3*((Z**2)/(A**(1/3))) -a4*((A-2*Z)**2)/A + a5/(A**(1/2))
        B_pernucleon = B/A
        #print(B_pernucleon)
        if B_pernucleon > B_pernucleon_optimum:
            B_pernucleon_optimum = B_pernucleon
            A_optimum = A
        
    optimum_bindings.append(B_pernucleon_optimum)

    print("The most stable isotope for Z =", Z, "is the one with A =", A_optimum)
    print("Its binding energy per nucleon is", B_pernucleon_optimum, "MeV")

print("And the most stable element would be Z =", (optimum_bindings.index(max(optimum_bindings)) + 1))
print("which has a binding energy of", max(optimum_bindings), "MeV")