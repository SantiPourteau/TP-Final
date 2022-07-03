import numpy as np
from typing import List

def translate_functions(modulation_type: str, modulation_parameters: List, x_value,sps):
    y=0
    if modulation_type == 'CONSTANT':
        y=1
    if modulation_type == 'LINEAR':
        y=(x_value/sps)/modulation_parameters[0]
    if modulation_type == 'INVLINEAR':
        y= max([(1 - ((x_value/sps)/modulation_parameters[0])),0])
    if modulation_type == 'SIN':
        y= 1 + (modulation_parameters[0]*np.sin(2*(np.pi)*(modulation_parameters[1]*(x_value/sps)))) 
    if modulation_type == 'EXP':
        y=np.exp((5*((x_value/sps)-modulation_parameters[0]))/modulation_parameters[0])
    if modulation_type == 'INVEXP':
        y= np.exp(-(5*(x_value/sps))/modulation_parameters[0])
    if modulation_type == 'QUARTCOS':
        y= np.cos((np.pi*(x_value/sps))/(2*modulation_parameters[0]))
    if modulation_type == 'QUARTSIN':
        y= np.sin((np.pi*(x_value/sps))/(2*modulation_parameters[0]))
    if modulation_type == 'HALFCOS':
        y=((1+(np.cos((np.pi*(x_value/sps))/(modulation_parameters[0]))))/2)
    if modulation_type == 'HALFSIN':
        y=(1+(np.cos(np.pi*(((x_value/sps)/(modulation_parameters[0]))-1))))/2
    if modulation_type == 'LOG':
        y=(np.log10(((9*(x_value/sps))/(modulation_parameters[0]))+1))
    if modulation_type == 'INVLOG':
        if x_value < modulation_parameters[0]:
            y= np.log10((((-9)*(x_value/sps))/(modulation_parameters[0]))+10)
        y=0
    if modulation_type == 'TRI':
        if x_value < modulation_parameters[1]:
            y=((x_value/sps)*(modulation_parameters[2]))/(modulation_parameters[1])
        if x_value > modulation_parameters[1]:
            y=( ((modulation_parameters[2])-1) * ( ((x_value/sps)-(modulation_parameters[1])) / ((modulation_parameters[1])-(x_value/sps)) ) ) + 1
    return y