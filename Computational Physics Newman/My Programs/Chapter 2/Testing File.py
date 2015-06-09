# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:02:18 2015

@author: Kike
"""

from numpy import loadtxt, array
from numpy import log as LOG
from math import log, exp

values = loadtxt("values.txt", float)
valueslist = list(map(log, values))
logs = array(valueslist, float)

geometric = exp(sum(logs)/len(logs))
print(geometric)

geometric2 = exp(sum(LOG(values))/len(values))
print(geometric2)