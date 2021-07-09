import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#load data file
data_layers= pd.read_excel('hemisphere layers.xlsx')


#load data into variables

l = data_layers['layer']

h = data_layers['height']
x1 = data_layers['x1']
x2 = data_layers['x2']
x3 = data_layers['x3']
x4 = data_layers['x4']
x5 = data_layers['x5']
layer1 = l[0:32:2]
layer2 = l[1:33:2]
layerall = l[1:33]
for x in layerall:
    layer = l[x]
    height = h[x]
    X1 = x1[x]
    X2 = x2[x]
    X3 = x3[x]
    X4 = x4[x]
    X5 = x5[x]
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
          ';;;;;;;;;;;;;;;; Layer ', layer, ';;;;;;;;;;;;;;;;','\n'
          ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;','\n'
          '                                             ')
    print('G3 	X0.00	Y-0.84	I-',X5,'  J-0.42 F5;','\n'
          'G1 	X0.84	Y0.84			          F5;','\n'
          'G3 	X0.00	Y-0.84	I-',X4,'  J-0.42 F5;','\n'
          'G1 	X-0.84	Y0.84			          F5;','\n'
          'G3 	X0.00	Y-0.84	I-',X3,'  J-0.42 F5;','\n'
          'G1 	X-0.84	Y0.84			          F5;','\n'
          'G3 	X0.00	Y-0.84	I-',X2,'  J-0.42 F5;','\n'
          'G1 	X-0.84	Y0.84			          F5;','\n'
          'G3 	X0.00	Y-0.84	I-',X1,'  J-0.42 F5;','\n')
    print('                                        ')
    print('G1	X0.00   Y0.840  Z0.6200		 F5;','\n'
          'G1	X-0.04  Y0.000  Z0.0000	 F5;','\n')
print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')    
print('G3 	X0.00	Y-0.84	I-',x1[32],'  J-0.42 F5;','\n'
'G1 	X0.84	Y0.84			          F5;','\n'
'G3 	X0.00	Y-0.84	I-',x2[32],'  J-0.42 F5;','\n'
'G1 	X-0.84	Y0.84			          F5;','\n'
'G3 	X0.00	Y-0.84	I-',x3[32],'  J-0.42 F5;','\n'
'G1 	X-0.84	Y0.84			          F5;','\n'
'G3 	X0.00	Y-0.84	I-',x4[32],'  J-0.42 F5;','\n'
'G1 	X-0.84	Y0.84			          F5;','\n'
'G3 	X0.00	Y-0.84	I-',x5[32],'  J-0.42 F5;','\n')


