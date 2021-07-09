# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:01:01 2018

@author: howell29
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#load data file
data_layers= pd.read_excel('hemisphere 2 layer.xlsx')


#load data into variables

l = data_layers['layer']

h = data_layers['height']
x1 = data_layers['x1']
x2 = data_layers['x2']
din = data_layers['din']

layer1 = l[0:32:2]
layer2 = l[1:33:2]
print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
';;;;;;;;;;;;;;;; Layer ', layer1[0], ';;;;;;;;;;;;;;;;','\n'
';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
'                                             ')
print('G3 	X0.00	Y-0.84	I-',x2[0],'  J-0.42 F5;','\n'
      'G1 	X0.84	Y0.84                 F5;','\n'
      'G3 	X0.00	Y-0.84	I-',x1[0],'  J-0.42 F5;','\n'
      )
for x in layer1:
    layer = l[x]
    layer_2= l[x+1]
    height = h[x]
    X1 = x1[x]
    X2 = x2[x]
    XX1 = x1[x+1]
    XX2 = x2[x+1]
    din1 = din[x-1]
    din2 = din[x]
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
          ';;;;;;;;;;;;;;;; Layer ', layer, ';;;;;;;;;;;;;;;;','\n'
          ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
          '                                             ')
    print('                                        ')
    print('G1	X0.00   Y0.840  Z0.6200		 F5;','\n'
          'G1	X-',din1,'  Y0.000  Z0.0000	 F5;','\n')
    print('G3 	X0.00	Y-0.84	I-',X1,'  J-0.42  F5;','\n'
          'G1 	X-0.84	Y0.84			 F5;','\n'
          'G3 	X0.00	Y-0.84	I-',X2,'  J-0.42  F5;','\n'
          '                                          ')
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
          ';;;;;;;;;;;;;;;; Layer ', layer_2, ';;;;;;;;;;;;;;;;','\n'
          ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
          '                                             ')
    print('                                        ')
    print('G1	X0.00   Y0.840  Z0.6200		 F5;','\n'
          'G1	X-',din2,'  Y0.000  Z0.0000	 F5;','\n')
    print('G3 	X0.00	Y-0.84	I-',XX2,'  J-0.42  F5;','\n'
          'G1 	X0.84	Y0.84			 F5;','\n'
          'G3 	X0.00	Y-0.84	I-',XX1,'  J-0.42  F5;','\n'
          '                                          ')
    
