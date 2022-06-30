import models.note_obj

class Music_Sheet():
    #music sheet va a guardar todas las notas del txt de partitura 
    def __init__(self, txt_sheet):
        self.note=[]
        with open(txt_sheet) as f:
            for line in f:
                time=line.split()[0]
                note=line.split()[1]
                duration=line.split()[2]
                self.note.append(models.note_obj.Note(time,note,duration))

    def get_note(self):
        return self.note


    

    

    
    