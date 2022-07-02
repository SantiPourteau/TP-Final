import models.note_obj

class Music_Sheet():
    #music sheet keep music sheet information
    def __init__(self, txt_sheet):
        self.note=[]
        with open(txt_sheet) as f: 
            
            data=[]
            for line in f:
                data.append(line.split()) #list of lists created
            data=sorted(data,key=lambda inner_list: int(inner_list[0])) #sorted based on start time
            contador=0
            for elem in data: #iteration over data to create instances of note object
                if contador==0: 
                    if elem[0] == 0:
                        time,note,duration=elem[0],elem[1],elem[2]
                        self.note.append(models.note_obj.Note(time,note,duration))
                    else:
                        #generate a note for inicial silence
                        time,note,duration=0,"None",elem[0]
                        self.note.append(models.note_obj.Note(time,note,duration))
                        #note after silence
                        time,note,duration=elem[0],elem[1],elem[2]
                        self.note.append(models.note_obj.Note(time,note,duration)) 
                if contador>0:
                    if elem[0]==time+duration:                     
                        time,note,duration=elem[0],elem[1],elem[2]
                        self.note.append(models.note_obj.Note(time,note,duration))
                    else:
                        #generate a note for silence moments
                        time=float(time)+float(duration)
                        note="None"
                        duration=abs(float(time)-int(elem[0]))
                        self.note.append(models.note_obj.Note(time,note,duration))
                        
                        #generate note after silence
                        time,note,duration=elem[0],elem[1],elem[2]
                        self.note.append(models.note_obj.Note(time,note,duration))

                contador+=1

    def get_note(self):
        #returns a list of all instances of note
        return self.note


    

    

    
    