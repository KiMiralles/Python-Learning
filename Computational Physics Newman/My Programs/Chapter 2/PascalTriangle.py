# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:04:18 2015

@author: Kike
"""

from BinomialCoefficients import binomial

# Number of lines of the Pascal triangle we want to print.
n = int(input("Enter the number of lines of the Pascal triangle you wish to see: "))

for each in range(1, n+1):
    for i in range(0, each+1):
        print(binomial(each, i), end=' ')
    print()
    

# An interesting remark: when I defined the function "binomial", I pre-defined
# also the function "factorial" to keep it shorter and more intuitive, so that
# "binomial" would simply call "factorial" to do its job. Interestingly, even
# though I only import "binomial" to this script, the function is able to call
# his much-needed sister "factorial" on its own, and so you have no need to
# specifically import it! (I'm guessing it's because they're on the same file.)