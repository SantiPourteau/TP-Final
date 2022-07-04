from logging import raiseExceptions
import pytest
from src.models.wave_obj import Wave
from src.models.instrument_obj import Instrument
from src.models.note_obj import Note
import numpy as np


def test_wave_get_waveform():
    #Given the note A4, starting point 1 and duration 1 second. 
    #Assert the given result to a.get_waveform
    #Due to the handling of small numbers, requires use of inequalities
    c = Note(1,'A4',1)
    a = Wave(c)
    b = Instrument('instrument.txt')
    assert int(a.get_waveform(1,b)) <= round(-3.99695004e-13)

