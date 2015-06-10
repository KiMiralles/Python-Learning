# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:26:18 2015

@author: Kike
"""

from BinomialCoefficients import binomial

# To calculate the probability of seeing AT LEAST v heads from n tosses, then
# the most sensible thing to do is to calculate 1 - prob(less than v heads from n tosses),
# which is easily done with a loop like this:

while True:
    n = int(input("How many times should we toss the coin? "))
    v = int(input("And how many times would you like, at least, to see heads? "))
    if n >= v:
        break
    else:
        print()
        print("You need to toss the coin at least the same number of times you wish to see heads!")
        print("Please, give sensible values to the program. Restarting...")
        continue

p_list = []
for i in range(0,v): # The count finishes at v-1, remember we want to see LESS THAN v!
    p = binomial(n,i) / 2**n
    p_list.append(p)
P = 1 - sum(p_list)  # P is the final probability!

print("The probability of seeing at least", v, "times heads when tossing a coin", n, "times is", P)