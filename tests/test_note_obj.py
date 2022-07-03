import pytest 
from src.models.note_obj import Note

def test_note():
    #Test if the given note returns a frequency
    a = Note(1,'A4',1)
    assert a.get_frequency() == 440.000
