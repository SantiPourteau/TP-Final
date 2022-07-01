import models.note_obj

class Music_Sheet():
    #music sheet va a guardar todas las notas del txt de partitura 
    def __init__(self, txt_sheet):
        self.note=[]
        with open(txt_sheet) as f:
            
            data=[]
            for line in f:
                data.append(line.split())
            data=sorted(data,key=lambda inner_list: inner_list[0])
            contador=0
            for elem in data:
                if contador==0:
                    time=elem[0]
                    note=elem[1]
                    duration=elem[2]
                    self.note.append(models.note_obj.Note(time,note,duration))
                if contador>0:
                    if elem[0]==time+duration:                     
                        time=elem[0]
                        note=elem[1]
                        duration=elem[2]
                        self.note.append(models.note_obj.Note(time,note,duration))
                    else:
                        #genera nota vaciaaa
                        time=float(time)+float(duration)
                        note="None"
                        duration=abs(float(time)-int(elem[0]))
                        self.note.append(models.note_obj.Note(time,note,duration))

                        time=elem[0]
                        note=elem[1]
                        duration=elem[2]
                        self.note.append(models.note_obj.Note(time,note,duration))

                contador+=1

    def get_note(self):
        return self.note


    

    

    
    