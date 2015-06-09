# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:37:25 2015

@author: Kike
"""

# Here we try to call the function. I will leave written two ways: one that
# tries to call it directly from here, and another that tries to fetch it from
# my desktop.

import sys
sys.path.insert(0, 'C:/Users/Kike/Desktop')  # From a StackOverflow answer.
# Python only searches the current directory, sys.path, and little more.
# So the trick to running from somewhere else relies on telling sys.path to
# add the new location to PYTHONPATH before running the program. That way,
# Python will also search for the folder you're talking about!

from FunctionTestFile import myfun as heyya

print(heyya(4))

from FUNC2 import myfun

print(myfun(5))