import models.note_obj

class Music_Sheet():
    def __init__(self, txt_sheet):
        with open(txt_sheet) as f:
            for line in f:
                time=line.split()[0]
                note=line.split()[1]
                duration=line.split()[2]
                self.note=models.note_obj.Note(time,note,duration)

#aca va a tener que poder recibir muchas notas. asi q el self.note va a ser una lista de Notas

    def get_note(self):
        return self.note


    

    

    
    