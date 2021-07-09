import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import itertools


data_layers = pd.read_excel('hemisphere cone python ready.xlsx')

layer = data_layers['layer']

p0 = data_layers['p0']
p1 = data_layers['p1']
p2 = data_layers['p2']
p3 = data_layers['p3']
p4 = data_layers['p4']
p5 = data_layers['p5']
p6 = data_layers['p6']
p7 = data_layers['p7']
p8 = data_layers['p8']
p9 = data_layers['p9']
p10 = data_layers['p10']
p11 = data_layers['p11']
p12 = data_layers['p12']
p13 = data_layers['p13']
p14 = data_layers['p14']

P = np.array([p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,
             p11,p12,p13,p14])

n0 = data_layers['n0']
n1 = data_layers['n1']
n2 = data_layers['n2']
n3 = data_layers['n3']
n4 = data_layers['n4']
n5 = data_layers['n5']
n6 = data_layers['n6']
n7 = data_layers['n7']
n8 = data_layers['n8']
n9 = data_layers['n9']
n10 = data_layers['n10']
n11 = data_layers['n11']
n12 = data_layers['n12']
n13 = data_layers['n13']
n14 = data_layers['n14']

N = np.array([n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,
             n11,n12,n13,n14])
#C = ["'r'","'g'","'b'","'c'"]
C = ['m','g','b','c']
fig = plt.figure(1, figsize=(40,20))
ax = fig.add_subplot(111)

for item1, item2, colors in zip(N,P,itertools.cycle(C)):
    for i in range(len(item1)):
        ax.plot(item1[i],layer[i],
                color = colors,
                marker = 'o',
                markersize=25)
        ax.plot(item2[i],layer[i],
                color = colors,
                marker = 'o',
                markersize=25)
plt.xlabel('Radius (mm)',fontsize=75)
plt.ylabel('Layer height (mm)',fontsize=75)
plt.xticks(size=60)
plt.yticks(size=60)
plt.grid(color='k', linestyle='-', linewidth=2)

plt.tight_layout()
plt.savefig('hemisphere internal cone.tiff')
plt.show()

import os
b1 = "hemisphere internal cone.tiff"
os.system("paint.exe" + b1)



