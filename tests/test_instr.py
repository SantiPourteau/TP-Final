from numpy import equal
import pytest
from src.models.instrument_obj import Instrument

@pytest.fixture
def txt_archive():
    #It returns the file descriptor of a given txt file
    #File descriptor is used so one can mention the given file 
    fd = open('test_textfile.txt','r')
    file = fd.fileno()
    fd.close()
    return file

def blank_txt(txt_archive):
    #Test the objects attributes given a blank test
    a = Instrument(txt_archive)
    assert a.get_num_harmonics() == None
    assert a.get_respective_amplitude(a.get_num_harmonics()) == None 
    assert a.get_attack() == None
    assert a.get_sustain() == None 
    assert a.get_decay() == None

def txt_with_given_numbers(txt_archive):
    #Test the objects attributes with a given note
    return 3

