from logging import raiseExceptions
import pytest
from src.models.wave_obj import Wave
from src.models.instrument_obj import Instrument
from src.models.note_obj import Note
import numpy as np


c = Note(0,'A4',1)
a = Wave(c)
b = Instrument('instrument.txt')
def test_wave_get_waveform():
    #Given the note A4, starting point 0 and duration 1 second. 
    #Calculate the waveform and compared to a.get_waveform 
    #Handling very small numbers required the use of inequalities and rounding
    
    assert int(a.get_waveform(1,b)) == 0


def test_case_wave():
    #test case wave with the same values
    assert int(a.case_wave(b,1)) == 0

