from note_obj import Note

class Music_Sheet():
    def __init__(self, txt_sheet):
        with open(txt_sheet) as f:
            for line in f:
                self.time=line.split()[0]
                self.note=line.split()[1]
                self.duration=line.split()[2]
                
    def get_time(self):
        return self.time
    def get_note(self):
        return self.note
    def get_duration(self):
        return self.duration


    

    

    
    