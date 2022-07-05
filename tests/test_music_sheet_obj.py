import pytest 
from src.models.music_sheet_obj import Music_Sheet
from src.models.note_obj import Note
from src.xylophone.xylo.note import XyloNote



def test_type_1(txt_archive):
    #Test if the Two objects are the same
    #Note1; start time = 0, note = G4, duration = 5
    #Note2; "            ", note = A4, "          "
    fd = open(txt_archive,'r')
    backup = fd.read()
    fd.close()
    lines = ['0 G4 5','0 A4 5']
    fd = open(txt_archive,'r+')
    for line in lines:
        fd.write(line)
        fd.write('\n')
    fd.close()

    a = Music_Sheet(txt_archive, 1)
    b = Note('0','G4','5')
    c = Note('0','A4','5')


    assert b.__eq__(a.get_note()[0]) == True
    assert c.__eq__(a.get_note()[1]) == True
    fd = open(txt_archive,'w')
    fd.write(backup)
    fd.close()
  


def test_type_2(txt_archive):
    #test if get_note() for the xylophone returns an instance of XyloNote
    fd = open(txt_archive,'r')
    backup = fd.read()
    fd.close()
    lines = ['0 G4 5','0 A4 5']
    fd = open(txt_archive,'r+')
    for line in lines:
        fd.write(line)
        fd.write('\n')
    fd.close()
    a = Music_Sheet(txt_archive,2)
    
    
    assert isinstance(a.get_note()[0],XyloNote)
    assert isinstance(a.get_note()[1],XyloNote)
    
    
    fd = open(txt_archive,'w')
    fd.write(backup)
    fd.close()


   
