# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:12:16 2015

@author: Kike
"""

from numpy import loadtxt
from pylab import xlabel, ylabel, show, scatter, xlim, ylim

data = loadtxt("stars.txt", float)

T = data[:,0]
Mag = data[:,1]

scatter(T,Mag)
xlabel("Temperature")
ylabel("Magnitude")
xlim(13000, 0)
ylim(20,-5)
show()