import pytest
from src.models.instrument_obj import Instrument
import os



def test_blank_txt(txt_archive):
    #Test the objects attributes given a blank test
    a = Instrument(txt_archive)
    assert a.get_num_harmonics() == None
    assert a.get_respective_amplitude(None) == None 
    assert a.get_attack() == None
    assert a.get_sustain() == None 
    assert a.get_decay() == None

def test_txt_with_one_note(txt_archive):
    #Test the attributes given a complete txt
    fd = open(txt_archive,'r')
    backup = fd.read()
    fd.close()
    lines = ['3','1 1.2','2 0.9','3 0.5', 'TRI 0.5 5 3','CONSTANT 1 5 7', 'INVLINEAR 3 2 1']
    fd = open(txt_archive,'r+')
    for line in lines:
        fd.write(line)
        fd.write('\n')
    
    fd.close()
    
    b = Instrument(txt_archive)
    assert b.get_num_harmonics() == 3
    assert b.get_respective_amplitude(1) == '1.2' 
    assert b.get_attack() == ['TRI', [0.5, 5.0, 3.0]]
    assert b.get_sustain() == ['CONSTANT', [1.0, 5.0, 5.0]]
    assert b.get_decay() == ['INVLINEAR',[3, 2, 1]]
    fd = open(txt_archive,'w')
    fd.write(backup)
    fd.close()
