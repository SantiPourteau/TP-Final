from note_obj import Note

class Partitura():
    def __init__(self, txt_partitura):
        with open(txt_partitura) as f:
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


    

    

    
    