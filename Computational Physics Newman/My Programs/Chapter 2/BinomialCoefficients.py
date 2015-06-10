# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:49:05 2015

@author: Kike
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1,n+1):
            f *= i
            #print(f)
        return f
        

def binomial(x,y):
    if x < y:
        print("ERROR: The first argument must be greater or equal to the second!")
    elif y == 0:
        return 1
    else:
        return int(factorial(x) / (factorial(y) * factorial(x-y)))

#number1 = int(input("Let's calculate the binomial coefficient of a pair of numbers. Enter the first integer: "))
#number2 = int(input("Now the second integer: "))

#print("The value of the binomial coefficient (", number1,",", number2, ") is", binomial(number1,number2))