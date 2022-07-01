import models.note_obj

class Music_Sheet():
    #music sheet va a guardar todas las notas del txt de partitura 
    def __init__(self, txt_sheet):
        self.note=[]
        with open(txt_sheet) as f:
            contador=0
            for line in f:
                if contador==0:
                    time=line.split()[0]
                    note=line.split()[1]
                    duration=line.split()[2]
                    self.note.append(models.note_obj.Note(time,note,duration))
                if contador>0:
                    if line.split()[0]==time+duration:                     
                        time=line.split()[0]
                        note=line.split()[1]
                        duration=line.split()[2]
                        self.note.append(models.note_obj.Note(time,note,duration))
                    else:
                        #genera nota vaciaaa
                        time=float(time)+float(duration)
                        note="None"
                        duration=abs(float(time)-int(line.split()[0]))
                        self.note.append(models.note_obj.Note(time,note,duration))

                        time=line.split()[0]
                        note=line.split()[1]
                        duration=line.split()[2]
                        self.note.append(models.note_obj.Note(time,note,duration))

                contador+=1

    def get_note(self):
        return self.note


    

    

    
    