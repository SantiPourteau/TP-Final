from note_obj import Note

class Music_Sheet():
    def __init__(self, txt_sheet):
        with open(txt_sheet) as f:
            for line in f:
                time=line.split()[0]
                note=line.split()[1]
                duration=line.split()[2]
                self.note=Note(time,note,duration)
                
    def get_note(self):
        return self.note


    

    

    
    