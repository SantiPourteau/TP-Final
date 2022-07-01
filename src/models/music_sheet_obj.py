import models.note_obj
from xylophone.xylophone.xylo.note import XyloNote

DELTA = 0.00001 # constant

class Music_Sheet():
    #music sheet va a guardar todas las notas del txt de partitura 
    def __init__(self, txt_sheet):
        with open(txt_sheet) as f:
            for line in f:
                time=line.split()[0]
                note=line.split()[1]
                duration=line.split()[2]
                self.note=models.note_obj.Note(time,note,duration)
            self.notes_metalofon = []

#aca va a tener que poder recibir muchas notas. asi q el self.note va a ser una lista de Notas

    def get_note(self):
        return self.note
    
    def filter_notes_metalofon(self,sheet):
        """
        Filters, Sorts and modifies if necessary the notes of the music sheet so they can be passed to a device.

        args:
            - sheet: Music sheet with start time, note and duration
        """
        accepted_notes = ['C7','C#7','Cb7','B6','Bb6','A6','A#6','Ab6','G6','G#6','Gb6','F6','F#6','E6','Eb6','D6','D#6','Db6','C6','C#6','B5','Bb5','A5','A#5','Ab5','G5','F5','E5','Eb5','D5','D#5','Db5','C5','C#5','B4','Bb4','A4','A#4','Ab4','G4','G#4']
        list = []
        with open(sheet,"r") as f:
            for line in f:
                line = line.strip('\n').split(' ')
                if line[1] in accepted_notes:
                    list.append([int(line[0]),line[1]])
                if line[1] not in accepted_notes:
                    raise ValueError('There is a note that is not supported by the xylophone.')
        list_sort = sorted(list)
        idx = 0
        while idx+1 < len(list):
            if list_sort[idx][0] == list_sort[idx+1][0]:
                list_sort[idx][0] += DELTA
            idx += 1
        list_final = sorted(list_sort)
        for _ in list_final:
                self.notes_metalofon.append(XyloNote(_[1],_[0],90))
        return self.notes_metalofon