# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:54:23 2019

@author: howell29
"""
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

currentDT = datetime.datetime.now()

""" INITIAL CODE """

f = open("hemisphere cone - SE 1700.txt","w+")

f.write(';Date and Time: {}\n'.format(str(currentDT)))    
f.write(';HOLLOW hemisphere - internal cone geometry w/ SE1700\n')
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
f.write(';Z-height = 0.75 * 0.5842 = 0.48315 \n')
f.write(';Height = (20mm/filament)/0.43815 mm = 34 filaments \n')

#load data file
data_layers = pd.read_excel('hemisphere cone python ready.xlsx')

'''
Constant Values
'''
speed = 10                                                              #mm/s
ext_width = 0.5842
half_width = round(ext_width/2,3)
z_height = round(0.75*ext_width,4)
din_cone = 0.444

#########################################################################
################ Loading Data from excel#################################
#########################################################################
L0 = data_layers['L0']
L1 = data_layers['L1']
L2 = data_layers['L2']
L3 = data_layers['L3']
L4 = data_layers['L4']
L5 = data_layers['L5']
L6 = data_layers['L6']
L7 = data_layers['L7']
L8 = data_layers['L8']
L9 = data_layers['L9']
L10 = data_layers['L10']
L11 = data_layers['L11']
L12 = data_layers['L12']
L13 = data_layers['L13']
L14 = data_layers['L14']
L15 = data_layers['L15']
L16 = data_layers['L16']
L17 = data_layers['L17']
L18 = data_layers['L18']
L19 = data_layers['L19']
L20 = data_layers['L20']
L21 = data_layers['L21']
L22 = data_layers['L22']
L23 = data_layers['L23']
L24 = data_layers['L24']
L25 = data_layers['L25']
L26 = data_layers['L26']
L27 = data_layers['L27']
L28 = data_layers['L28']
L29 = data_layers['L29']

L30 = data_layers['L30']
L31 = data_layers['L31']
L32 = data_layers['L32']
L33 = data_layers['L33']
L34 = data_layers['L34']
L35 = data_layers['L35']
L36 = data_layers['L36']
L37 = data_layers['L37']
L38 = data_layers['L38']
L39 = data_layers['L39']
L40 = data_layers['L40']
L41 = data_layers['L41']
L42 = data_layers['L42']
L43 = data_layers['L43']
L44 = data_layers['L44']

din1 = data_layers['din1']
din2 = data_layers['din2']
din3 = data_layers['din3']
din4 = data_layers['din4']
din5 = data_layers['din5']
din6 = data_layers['din6']
din7 = data_layers['din7']
din8 = data_layers['din8']
din9 = data_layers['din9']
din10 = data_layers['din10']
din11 = data_layers['din11']
din12 = data_layers['din12']
din13 = data_layers['din13']
din14 = data_layers['din14']
din15 = data_layers['din15']
din16 = data_layers['din16']
din17 = data_layers['din17']
din18 = data_layers['din18']
din19 = data_layers['din19']
din20 = data_layers['din20']
din21 = data_layers['din21']
din22 = data_layers['din22']
din23 = data_layers['din23']
din24 = data_layers['din24']
din25 = data_layers['din25']
din26 = data_layers['din26']
din27 = data_layers['din27']
din28 = data_layers['din28']
din29 = data_layers['din29']
din30 = data_layers['din30']
din31 = data_layers['din31']
din32 = data_layers['din32']
din33 = data_layers['din33']
din34 = data_layers['din34']
din35 = data_layers['din35']
din36 = data_layers['din36']
din37 = data_layers['din37']
din38 = data_layers['din38']
din39 = data_layers['din39']
din40 = data_layers['din40']
din41 = data_layers['din41']
din42 = data_layers['din42']
din43 = data_layers['din43']
din44 = data_layers['din44']

dup1 = data_layers['dup1']
dup2 = data_layers['dup2']
dup3 = data_layers['dup3']
dup4 = data_layers['dup4']
dup5 = data_layers['dup5']
dup6 = data_layers['dup6']
dup7 = data_layers['dup7']
dup8 = data_layers['dup8']
dup9 = data_layers['dup9']
dup10 = data_layers['dup10']
dup11 = data_layers['dup11']
dup12 = data_layers['dup12']
dup13 = data_layers['dup13']
dup14 = data_layers['dup14']
dup15 = data_layers['dup15']
dup16 = data_layers['dup16']
dup17 = data_layers['dup17']
dup18 = data_layers['dup18']
dup19 = data_layers['dup19']
dup20 = data_layers['dup20']
dup21 = data_layers['dup21']
dup22 = data_layers['dup22']
dup23 = data_layers['dup23']
dup24 = data_layers['dup24']
dup25 = data_layers['dup25']
dup26 = data_layers['dup26']
dup27 = data_layers['dup27']
dup28 = data_layers['dup28']
dup29 = data_layers['dup29']
dup30 = data_layers['dup30']
dup31 = data_layers['dup31']
dup32 = data_layers['dup32']
dup33 = data_layers['dup33']
dup34 = data_layers['dup34']
dup35 = data_layers['dup35']
dup36 = data_layers['dup36']
dup37 = data_layers['dup37']
dup38 = data_layers['dup38']
dup39 = data_layers['dup39']
dup40 = data_layers['dup40']
dup41 = data_layers['dup41']
dup42 = data_layers['dup42']
dup43 = data_layers['dup43']
dup44 = data_layers['dup44']

L = np.array([L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,
             L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,
             L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,
             L31,L32,L33,L34,L35,L36,L37,L38,L39,L40,
             L41,L42,L43,L44])

DIN = np.array([din1,din2,din3,din4,din5,din6,din7,din8,din9,din10,
             din11,din12,din13,din14,din15,din16,din17,din18,din19,din20,
             din21,din22,din23,din24,din25,din26,din27,din28,din29,din30,
             din31,din32,din33,din34,din35,din36,din37,din38,din39,din40,
             din41,din42,din43,din44])

DUP = np.array([dup1,dup2,dup3,dup4,dup5,dup6,dup7,dup8,dup9,dup10,
             dup11,dup12,dup13,dup14,dup15,dup16,dup17,dup18,dup19,dup20,
             dup21,dup22,dup23,dup24,dup25,dup26,dup27,dup28,dup29,dup30,
             dup31,dup32,dup33,dup34,dup35,dup36,dup37,dup38,dup39,dup40,
             dup41,dup42,dup43,dup44])

    
counter = 1         #counter for layer height
counter2 = 0        #counter for perimeter
counter3 = 0        #counter for detrming first 
                            #perimeter, middle perimeters and last perimeters
                            

#initialize
f.write(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')
f.write(';;;;;;;;;;;;;;;; Layer {} ;;;;;;;;;;;;;;;;;;\n'.format(counter))
f.write(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')
f.write('                                             \n')

f.write(';;;;;;;;;;;;;;; Perimeter {} ;;;;;;;;;;;;;;; \n'.format(1))
f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION\n'
    .format(ext_width, round(L0[0]-ext_width,3), half_width, speed))
f.write('G1 X{} Y{} Z0.00 F{}; \n'
        .format(ext_width, ext_width, speed))
f.write(';;;;;;;;;;;;;;; Perimeter 2 ;;;;;;;;;;;;;;; \n')
f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION\n'.format(ext_width,
        L0[0],half_width,speed))

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
for list1, list2, list3 in zip(L[1:], DIN, DUP):  
    #print(counter)
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

    f.write('G1 X0.00 Y{} Z{} F{}; MOVE UP LAYER\n'.format(ext_width,
          z_height,speed))
    even_odd = (-1)**counter
    #f.write(';even/odd counter = {}\n'.format(even_odd))
    if even_odd > 0:        #For when the layer is moving inward for each 
                            #additional perimeter

        for i in range(len(list1)):

            if list1[i] > 0: 
                if list1[i] >= 20:
                    break
                len_list1 = len(nonzerolist1)
                               
                counter2 = counter2 + 1
                counter3 = counter3 + 1
                f.write('                                                \n')
                f.write(';;;;;;;;;;;;;;; Perimeter {} ;;;;;;;;;;;;;;; \n'.format(counter2))
#                f.write(';List1 = {}; list2 = {}; list3 = {}, i = {}\n'
#                        .format(round(list1[i],3),round(list2[i],3),round(list3[i],3),i))
                if counter4 < 1:
                    f.write('G1 X-{} Y0.00 Z0.00 F{}; PERIMETER DIFFERENCE L[i] and L[i-1] \n'
                            .format(round(list3[i],3),speed))

                elif 1 <= counter4 < len(nonzerolist1)-1:
                    if list2[i-1] <= 0:
                        break
                    #perim_diff_within_layer = round(list1[i] - list1[i+1],3) 
                    f.write('G1 X-{} Y0.00 Z0.00 F{}; Move inward\n'
                            .format(round(list2[i-1],3),speed))                    
                    f.write('G1 X0.00 Y{} Z0.00 F{}; MOVE INWARD\n'
                            .format(ext_width,speed))
#                    print('x = -',round(list2[i-1],3))
                else:
                    f.write(';MARKER\n')
                    f.write('G1 X-{} Y0.00 Z0.00 F{}; Move inward\n'
                            .format(round(list2[i-1],3),speed))
                    f.write('G1 X0.00 Y{} Z0.00 F{}; CIRCULAR ALIGNMENT\n'
                            .format(ext_width,speed))
                    counter2 = 0
                    
                    
                f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION\n'
                        .format(ext_width,round(list1[i],3),half_width,speed))
                                
#                print(list1[i])
                counter4 = counter4 + 1
                
            else:
                counter2 = 0
                counter4 = 0
                break
    else:
        for i in range(len(list1)):


            if list1[i] > 0:
                if list1[i] >= 20:
                    break
                if i > (len(new_reverse_list1)-1):
                    break

                counter2 = counter2 + 1
                counter3 = counter3 + 1
                f.write('                                               \n')
                f.write(';;;;;;;;;;;;;;; Perimeter {} ;;;;;;;;;;;;;;;\n'.format(counter2))
                #f.write(';Counter 4 = {} \n'.format(counter4))
#                f.write(';List1 = {}; list2 = {}; list3 = {}, i = {}\n'
#                        .format(round(list1[i],3),round(list2[i],3),round(list3[i],3),i))
                if counter4 < 1:
                    f.write('G1 X-{} Y0.00 Z0.00 F{}; \n'
                            .format(din_cone,speed))
                    f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION \n'
                        .format(ext_width,round(last_perimeter,3),half_width,speed))
#                    print(last_perimeter)

                elif 1 <= counter4 < len(new_reverse_list1)-1:
                    perim_diff_within_layer = round(list1[i]-list1[i+1],3)
                    f.write('G1 X{} Y0.00 Z0.00 F{}; OUTWARD MOVE\n'
                            .format(round(list2[i-1],3),speed))
                    f.write('G1 X0.00 Y{} Z0.00 F{};        OUTWARD MOVE \n'
                            .format(ext_width,speed))
#                    print('x = ',round(list2[i-1],3))
                    f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION \n'
                            .format(ext_width,round(new_reverse_list1[i],3),half_width,speed))
#                    print(new_reverse_list1[i])
                else:
                    f.write(';MARKER2\n')
                    #perim_diff_within_layer = round(list1[i]-list1[i+1],3)    
                    f.write('G1 X{} Y0.00 Z0.00 F{}; OUTWARD MOVE\n'
                            .format(perim_diff_within_layer,speed))
                    f.write('G1 X0.00 Y{} Z0.00 F{};        CIRCULAR ALIGNMENT \n'
                            .format(ext_width,speed))
                    f.write('G3 X0.00 Y-{} I-{} J-{} F{}; CIRCULAR MOTION \n'
                            .format(ext_width,round(new_reverse_list1[i],3),half_width,speed))
                f.write('  \n')
                    
                counter4 = counter4 + 1    
                
            else: 
                counter2 = 0
                counter4 = 0 
                break
#
#        else:
#            counter2 = 0
#            counter3 = 0
#            counter4 = 0 
#            break
        
f.write('CALL TogglePress P1; Turn pressure box on\n')
f.write('G1 Y15.00 Z5.00 F50\n')        
f.close()
import os
b1="hemisphere cone - SE 1700.txt"
os.system('notepad.exe ' + b1)


  