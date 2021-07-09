# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:01:40 2019

@author: howell29
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime
import itertools
'''
The following code is split up into multiple sections. 

Section 1: Operations
All of the calculations are performed in the first section. Each function 
defines an operation for a given array. 

Section 2: Constants
This defines all of the initial parameters and constants. Here, changes to the 
dimensions of the hemi, nozzle size, and threshold (minimum distance between
each adjacent concentric circle) can be made. 

Section 3: Arrays for calculations 
Arrays based on the previously defined funtions are made here. These arrays 
consist of the base calculations for graphing purposes

Section 4: Arrays for G-Code
Arrays also based on previously defined functions are made here. The purposes 
of theses calculations are to produce the necessary vectors for th G-Code

Section 5: Graphing section
Most computationally expensive part of the code. Comment out if only the G-Code
is needed

Section 6: G-Code generation
By far the most complicated part of the code. Don't fuck this part -- very 
fragile.


CONFIRM GENERATED G-CODE IN SIMLUATION 
'''
################################################################################################################################################
''' 
Section 1: Operations
'''
''' Where input x:= layer # '''
def layer_height(x):                                                            
    height = z_height + x*z_height
    return height

def perimeter_hemisphere(x):                                                    
    perim_hemi = np.sqrt(hemisphere_height**2 - x**2)
    return perim_hemi

''' Where input x := layer # '''
def perimeter_cone(x):                                                         
#    perim_cone = outer_radius - x * z_height
    perim_cone = outer_hemisphere[0] - x * z_height
    return perim_cone

''' Where input x:= layer # '''
def perimeter_hemi(x):
    hemi_arr = []
    for i in range(len(x)):
        if x[i] < hemi_height:
            output_hemi = np.sqrt(hemi_height**2 - x[i]**2)

#        elif x[i] >= hemi_height: 
#            output_hemi = round(inner_cone[-1],4)
        hemi_arr.append(output_hemi)
#    print('hemi_arr = ',hemi_arr)
    return hemi_arr
''' Where input x := the difference between the outter perimeter
and the inner perimeter '''                   
def tot_perimeters_layer(x):                                                   
    arr1 = []                                                                              
    for i in range(len(x)):

        if x[i] > threshold:
            y = int(
                    np.rint(
                    (x[i] - threshold) / threshold) 
                    )
        elif x[i] <= threshold: 
            y = 0 
        arr1.append(y)         
    return arr1    
''' Most important function. Inputs: cone, hemi, total_perims := inner perimeter
of cone, outer perimeter of hemisphere, total required perimeters in between
the inner and outer perimeters. 
'''
def perimeter_arrays(cone, hemi, total_perims):                                 
    perim_arrays = []
    counter = 0
    for i, j, k in zip(cone, hemi, total_perims):
        empty_arr = []
        if i == j :
            empty_arr.append(i)
            perim_arrays.append(empty_arr)
        elif k < 1: 
            empty_arr.append(j)
            empty_arr.append(i)
            perim_arrays.append(empty_arr)
        elif k >= 1: 
            for x in range(0,k+2,1):
                if x == 0:
                    empty_arr.append(j)
                elif x <= k:
                    empty_arr.append(j - x * ((j-i)/(k+1)))
                elif x > k:
                    empty_arr.append(i)
            perim_arrays.append(empty_arr)
        counter = counter + 1
    return perim_arrays

def n_perimeter_arrays(perim_arrays):
    perim_array_tot = []
    for i in perim_arrays:
        perim_array_ind = []
        for j in i: 
            perim_array_ind.append(-1 * j)
        perim_array_tot.append(perim_array_ind)
    return perim_array_tot

# COLORS for GRAPHING
def color_cycle(iterable):
    # C = ['m','g','b','c']
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

# LIST1 = PERIMETERS
# LIST2 = ARRAY OF HORIZONTAL MOVES BETWEEN CONCENTRIC PERIMETERS
        # WITHIN EACH LAYER
def horizontal_moves(perims):
    horizontal_mat = []
    for i, item in enumerate(perims):
        horizontal_ind = []
        if len(item) > 1: 
            for j, value in enumerate(item):
                if j < len(item) - 1:
                    horizontal_ind.append(item[j]-item[j+1])
        horizontal_mat.append(horizontal_ind)
    return horizontal_mat
# lIST3 = ARRAY OF HORIZONTAL MOVES BETWEEN OUTER PERIMETER OF THE 
        # THE FIRST PERIMETER AND THE OUTER PERIMETER OF THE SECOND 
        # -- THE ONLY VALUES THAT ARE NEED ARE THE OUTER LAYERS . 
        # THE INNER LAYERS ARE ALREADY DETERMINED BY THE LINEAR RELATION
        # OF A CONE. THE OUTER LAYERS ARE DETERMINED BY SQRT(X^2-Y^2)
        
def vertical_moves(perims):
    vertical_mat = []
    for i, item in enumerate(perims):
        vertical_ind = []
#        print('i = {}'.format(i))
        if i >= len(perims)-1:
#            print('marker1')
            break
        elif len(item) <= len(perims[i+1]):
#            print('marker2')
            for j, value in enumerate(item):
#                print('marker3 i = {}, j = {}'.format(i,j))
                vertical_ind.append(value - perims[i+1][j])
#            vertical_mat.append(vertical_ind)
        elif len(item) >= len(perims[i+1]):
            for j, value2 in enumerate(item):
#                print('marker4 i = {}, j = {}'.format(i,j))
#                print(len(perims[i+1]))
                
                if j < len(perims[i+1]):
#                    print('perims[i+1][j] = {}'.format(perims[i+1][j]))
                    vertical_ind.append(value2 - perims[i+1][j])
#                    print(vertical_ind)
                elif j >= len(perims[i+1]):
#                    print('BREAK2')
                    break

        vertical_mat.append(vertical_ind)
#    print(vertical_mat)
    return vertical_mat

def vertical_moves_2(perims):
    vertical_mat = []
    for i, item in enumerate(perims):
        if i >= len(perims)-1:
            break
        else:
            vertical_mat.append(item[-1] - perims[i+1][-1])
    return vertical_mat


def pretty_arr(x):
    for i, item in enumerate(x):
#        print('i = {}'.format(i))
        print(" ".join(map(str,item)))
            
################################################################################################################################################           
''' 
Section 2: Constants
'''

speed = 15                                                                      # mm/s 
ext_width = 0.838                                                               # mm (nozzle width)
thickness = 5 - ext_width/2
half_width = round(ext_width/2, 4)                                              # mm
z_height = round(0.75*ext_width,3)                                              # mm 

''' Dimensions of hemisphere
'''
outer_radius = 15 + half_width                                                  # mm
hemisphere_height = outer_radius                                                # mm
hemi_height = hemisphere_height - thickness

tot_layers = int(
        np.floor(hemisphere_height/z_height) #floor
        )

threshold = round(1.1 * ext_width, 4)                                           # defines the threshold for required
                                                                                # distance of roadwidth (center of filament
                                                                                # to center of adjacent filament)
half_thresh = round(threshold/2,4)
din_cone = z_height #0.444                                                      # Inward move distance required to 
                                                                                # create the internal conical shape

################################################################################################################################################
''' 
Section 3: Arrays for calculations
'''
layer = np.linspace(0,tot_layers-1, tot_layers)   
#empty_arr = []     
height = layer_height(layer)
outer_hemisphere = perimeter_hemisphere(height)
inner_hemi = perimeter_hemi(height)
#inner_cone = np.linspace(20, 0, tot_layers)
#inner_cone =  perimeter_cone(layer)                                             # Difference between each additional layer = 0.43815

#inner_hemi = np.ones(len(inner_cone)) = 

hemi_cone_diff = np.round(outer_hemisphere-inner_hemi,2)

tot_perims_layer = tot_perimeters_layer(hemi_cone_diff)

perimeters = perimeter_arrays(inner_hemi, outer_hemisphere, tot_perims_layer)
n_perimeters = n_perimeter_arrays(perimeters)
################################################################################################################################################
'''
Section 4: Arrays for G-Code
'''
L = perimeters
DIN = horizontal_moves(perimeters)
DUP = vertical_moves(perimeters)
DUP_2 = vertical_moves_2(perimeters)
ALL = [L,DIN,DUP]
# Write arrays to excel sheet for easy viewing
df1 = pd.DataFrame(L)
df2 = pd.DataFrame(DIN)
df3 = pd.DataFrame(DUP)

filepath = 'main_parameters_nothresh.xlsx'
writer = pd.ExcelWriter(filepath, engine='xlsxwriter')

df1.to_excel(writer, sheet_name='Layer')
df2.to_excel(writer, sheet_name='Horizontal')
df3.to_excel(writer, sheet_name='Vertical')
writer.save()
################################################################################################################################################
''' 
Section 5: Graphing section
'''
C = ['m','g','b','c']
colors = itertools.cycle(C)

plt.figure(1, figsize=(40,20))
x = 0 
for i, (item1, item2) in enumerate(zip(perimeters,n_perimeters)):
    c = next(colors)
    for value1, value2 in zip(item1, item2):
        
        plt.plot(value1, layer[i], marker='o',color = c,markersize=15)
        plt.plot(value2, layer[i], marker='o',color = c,markersize=15)
        
plt.xlabel('Radius (mm)',fontsize=75)
plt.ylabel('Number of filaments (#)',fontsize=75)
plt.xticks(size=60)
plt.yticks(size=60)
plt.grid(color='k', linestyle='-', linewidth=2)

plt.tight_layout()
plt.savefig('hemisphere internal hemi - optimized.tiff')
plt.show()

################################################################################################################################################  
'''
Section 6: G-Code generation
'''

currentDT = datetime.datetime.now()

""" INITIAL CODE """

f = open("hemisphere internal hemi GREEN TIP.txt","w+")

f.write(';Date and Time: {}\n'.format(str(currentDT)))    
f.write(';optimized HOLLOW hemisphere - internal cone geometry w/ SE1700\n')
f.write('GREEN TIP \n')
f.write('                                             \n')
f.write(r'#include "C:\Users\howell29\Desktop\ULTIMUSV.PGM"' + os.linesep)
f.write('CALL SetPress Q25 P1; Try dropping back to 28\n')
f.write('CALL TogglePress P1; Turn pressure box on\n')
f.write('                                             \n')
f.write('G108; VELOCITY ON\n')
f.write('G91;  INCREMENTAL\n')
f.write('                                             \n')

f.write('DWELL 0.25; 		Accounts for ink lag, change as necessary\n')
f.write('                                             \n')
f.write(';Z-height = 0.75 * 0.838 = 0.6285 \n')
f.write(';Height = (20mm/filament)/0.43815 mm = 34 filaments \n')

counter = 0         #counter for layer height
counter2 = 0        #counter for perimeter
counter3 = 0        #counter for detrming first 
                    #perimeter, middle perimeters and last perimeters                            
#initialize
#f.write(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')
#f.write(';;;;;;;;;;;;;;;; Layer {} ;;;;;;;;;;;;;;;;;;\n'.format(counter))
#f.write(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')
#f.write('                                             \n')
#
#f.write(';;;;;;;;;;;;;;; Perimeter {} ;;;;;;;;;;;;;;; \n'.format(1))
#f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION\n'
#    .format(threshold, round(perimeters[0][0]-threshold,3), half_thresh, speed))
#f.write('G1 X{} Y{} Z0.00 F{}; \n'
#        .format(threshold, threshold, speed))
#f.write(';;;;;;;;;;;;;;; Perimeter 2 ;;;;;;;;;;;;;;; \n')
#f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION\n'.format(threshold,
#        round(perimeters[0][0],3),half_thresh,speed))

f.write('                                        \n')

"""
list1 = array of concentric circles for each individual layer
list2 = array of horizontal moves between each concentric perimeter 
        w/in each layer
list3 = array of horizontal moves between outer perimeter of the 
        first layer and the outer perimeter of the second
        -- the only values that are need are the outer layers. The
        inner layers are already determined by the linear relation
        of a cone. The outer layers are determined by sqrt(x^2 - y^2)
"""
                    
#For some reason DIN is creating an empty [] in the first position. 
#Skipping for now unit I can figure out what is going on with horizontal moves function                                            
for index, (list1, list2, list3) in enumerate(zip(L[1:],DIN[1:],DUP)):                             
    counter = counter + 1
    counter4 = 0 
    nonzerolist1 = [i for i, e in enumerate(list1) if e !=0]
    last_value = nonzerolist1[-1]
    last_perimeter = list1[last_value]
    reverse_list1 = list1[::-1]
    new_reverse_list1 = np.trim_zeros(reverse_list1)

    f.write(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')
    f.write(';;;;;;;;;;;;;;;; Layer {} ;;;;;;;;;;;;;;;;;;\n'.format(counter))
    f.write(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')

    f.write('G1 X0.00 Y{} Z{} F{}; MOVE UP LAYER\n'.format(threshold,
          z_height,speed))
    
    even_odd = (-1)**counter
    if even_odd < 0: 
        for i in range(len(list1)):
            if list1[i] >= L[0][0]:                                              #skips first layer
                print('line 323')
                break
            
            if counter2 > len(list1):
                counter2 = 0 
                counter4 = 0
                break
            
            counter2 = counter2 + 1
            counter3 = counter3 + 1
            f.write('                                           \n')
            f.write(';;;;;;;;;;;;;;; Perimeter {} ;;;;;;;;;;;;;;; \n'
                    .format(counter2))
#            f.write('counter = {}, counter2 = {}, counter4 = {} \n'
#                    .format(counter, counter2, counter4))
            if counter4 < 1:                                                    # for the first term in each layer
                f.write('G1 X-{} Y0.00 Z0.00 F{}; PERIMETER DIFFERENCE L[i] and L[i-1] \n'
                            .format(round(list3[i],3),speed))
#                print(list3[i])
                
            elif 1 <= counter4 < len(list1) - 1:
                if list2[i-1] <= 0:
                    print('elif break line 335 counter = {}'
                          .format(counter))
                    break
                f.write('G1 X-{} Y0.00 Z0.00 F{}; Move inward\n'
                        .format(round(list2[i-1],3),speed))                    
                f.write('G1 X0.00 Y{} Z0.00 F{}; MOVE INWARD\n'
                        .format(threshold,speed)) 
                
            else: 
                f.write(';MARKER \n')
#                print('counter = {}, counter2 = {}'.format(counter, counter2))
                f.write('G1 X-{} Y0.00 Z0.00 F{}; Move inward\n'
                        .format(round(list2[i-1],3),speed))
                f.write('G1 X0.00 Y{} Z0.00 F{}; CIRCULAR ALIGNMENT\n'
                        .format(threshold,speed))
                counter2 = 0

            f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION\n'
                    .format(threshold,round(list1[i],3),half_thresh,speed))  
            counter4 = counter4 + 1 
    elif even_odd > 0:
        for i in range(len(reverse_list1)):
#            print('range(len(reverse_list1)) = {}'.format(range(len(reverse_list1))))
            if reverse_list1[i] >= L[0][0]:
                print('break at 375')
                break
            if i > len(reverse_list1)-1: 
                print('break at 378')
                break
#            print('reverse_list1 = {}'.format(reverse_list1))
            counter2 = counter2 + 1
            counter3 = counter3 + 1
            f.write('                                               \n')
            f.write(';;;;;;;;;;;;;;; Perimeter {} ;;;;;;;;;;;;;;;\n'
                    .format(counter2))
            f.write(';Counter4 = {}\n'.format(counter4))
            
            if counter4 < 1: 
                f.write('G1 X-{} Y0.00 Z0.00 F{}; \n'
                        .format(DUP_2[index],speed))
#                print('i = {}, DUP_2[i] = {}'.format(i,DUP_2[i]))
                f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION \n'
                    .format(threshold,round(reverse_list1[i],3),half_thresh,speed))     
            elif 1 <= counter4 < len(reverse_list1)-1:
                perim_diff_within_layer = round(reverse_list1[i+1]-reverse_list1[i],3)
                f.write('G1 X{} Y0.00 Z0.00 F{}; OUTWARD MOVE \n'
                        .format(round(list2[i-1],3),speed))
                f.write('G1 X0.00 Y{} Z0.00 F{};        OUTWARD MOVE \n'
                        .format(threshold,speed))
                f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION \n'
                        .format(threshold,round(reverse_list1[i],3),half_thresh,speed)) 
            
            else:
                perim_diff_within_layer = round(reverse_list1[i]-reverse_list1[i-1],3)
                f.write(';MARKER2 \n')
                f.write('G1 X{} Y0.00 Z0.00 F{}; OUTWARD MOVE \n'
                        .format(perim_diff_within_layer,speed))
                f.write('G1 X0.00 Y{} Z0.00 F{}; CIRCULAR ALIGNMENT \n'
                        .format(threshold,speed))
                f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION \n'
                        .format(threshold, round(reverse_list1[i],3),half_thresh,speed))
            f.write('   \n')
        
            counter4 = counter4 + 1
        
    
    counter2 = 0 
    counter4 = 0 
       
f.write('CALL TogglePress P1; Turn pressure box off \n')
f.write('G1 Y15.00 Z5.00 F50; \n')
f.close()
import os
b1 = 'hemisphere internal hemi GREEN TIP.txt'
os.system('notepad.exe ' + b1)
        
 
