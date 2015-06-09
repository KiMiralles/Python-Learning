# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:02:18 2015

@author: Kike
"""

mylist = [1, 2, 3, 4]

for each in mylist:
    if each == 3:
        continue
    print(each)
print("Finished!")

for each in mylist:
    if each == 3:
        print("I hate the number three! I won't continue executing the program.")
        break
    print(each)
else:
    print("Program finished correctly")
print("Program did not finish entirely!!")