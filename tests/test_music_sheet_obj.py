import pytest 
from src.models.music_sheet_obj import Music_Sheet
from src.models.note_obj import Note



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
  

'''
def test_type_2():
    a = Music_Sheet('partitura.txt',2)
    assert a.get_note() == 0
'''   
   
