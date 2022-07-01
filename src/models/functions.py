import numpy as np
from typing import List, Array

def translate_functions(attack: str, att_parameters: List, los_x: Array):
    if attack == 'CONSTANT':
        return 1
    if attack == 'LINEAR':
        return (los_x)/att_parameters[0]
    if attack == 'INVLINEAR':
        return 1 - ((los_x)/att_parameters[0])
    if attack == 'SIN':
        return 1 + (att_parameters[0]*np.sin(2*(np.pi)*(att_parameters[1]*los_x)))
    if attack == 'EXP':
        return np.exp((5*(los_x-att_parameters[0]))/att_parameters[0])
    if attack == 'INVEXP':
        return np.exp(-(5*(los_x))/att_parameters[0])
    if attack == 'QUARTCOS':
        return np.cos((np.pi*(los_x))/(2*att_parameters[0]))
    if attack == 'QUARTSIN':
        return np.sin((np.pi*(los_x))/(2*att_parameters[0]))
    if attack == 'HALFCOS':
        return (1+(np.cos((np.pi*(los_x))/(att_parameters[0]))))/2
    if attack == 'HALFSIN':
        return (1+(np.cos(np.pi*(((los_x)/(att_parameters[0]))-1))))/2
    if attack == 'LOG':
        return np.log10(((9*(los_x))/(att_parameters[0]))+1)
    if attack == 'INVLOG':
        if los_x < att_parameters[0]:
            return np.log10((((-9)*(los_x))/(att_parameters[0]))+10)
        return 0
    if attack == 'TRI':
        if los_x < att_parameters[1]:
            return ((los_x)*(att_parameters[2]))/(att_parameters[1])
        if los_x > att_parameters[1]:
            return ( ((att_parameters[2])-1) * ( ((los_x)-(att_parameters[1])) / ((att_parameters[1])-(los_x)) ) ) + 1