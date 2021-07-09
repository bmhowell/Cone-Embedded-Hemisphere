# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:41:11 2018

@author: howell29
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#load data file
data_layers= pd.read_excel('hemisphere base layer.xlsx')

#load data innto variables

circle = data_layers['circle']
diameter = data_layers['diameter']
I_position = data_layers['I']

for x in I_position:
#    d = diameter[x]
#    c = circle[x]
    i = I_position[x]
    print('G3   X0.00   Y-0.84  I',i,'J-0.42    F15;','\n',
          'G1   X0.84   Y0.84   I0.00   J0.00   F15;')
    
    