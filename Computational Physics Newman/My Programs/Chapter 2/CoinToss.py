# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:15:54 2015

@author: Kike
"""

from BinomialCoefficients import binomial

while True:
    n = int(input("How many times should we toss the coin? "))
    v = int(input("And how many times would you like to see heads? "))
    if n >= v:
        break
    else:
        print("You need to toss the coin at least the same number of times you wish to see heads!")
        print("Please, give sensible values to the program. Restarting...")
        continue

p = binomial(n,v) / 2**n
print("The probability of seeing", v, "times heads when tossing a coin", n, "times is", p)

# To calculate the probability of seeing AT LEAST v heads from n tosses, then
# the most sensible thing to do is to calculate 1 - prob(less than v heads from n tosses),
# which is easily done with a loop like this:
# p_list = []
# for i in range(0,v+1):
#     p = binomial(n,i) / 2**n
#     p_list.append(p)
# P = 1 - sum(p_list)  # P is the final probability!