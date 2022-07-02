import models.note_obj
from xylophone.xylophone.xylo.note import XyloNote
DELTA = 0.00001
VELOCITY = 90
class Music_Sheet():
    #music sheet keep music sheet information
    def __init__(self, txt_sheet,type):
        self.note=[]
        self.type = type
        with open(txt_sheet) as f: 
            
            data=[]
            for line in f:
                data.append(line.split()) #list of lists created
            data=sorted(data,key=lambda inner_list: inner_list[0]) #sorted based on start time
            if self.type == 1:
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
            elif self.type == 2:
                accepted_notes = ['C7','C#7','Cb7','B6','Bb6','A6','A#6','Ab6','G6','G#6','Gb6','F6','F#6','E6','Eb6','D6','D#6','Db6','C6','C#6','B5','Bb5','A5','A#5','Ab5','G5','F5','E5','Eb5','D5','D#5','Db5','C5','C#5','B4','Bb4','A4','A#4','Ab4','G4','G#4']
                list = []
                for _ in data:
                    if _[1] in accepted_notes:
                        list.append([int(_[0]),_[1]])
                    if _[1] not in accepted_notes:
                        raise ValueError(f'{_[1]} is not in accepted notes')
                list_sort = sorted(list)
                idx = 0
                list_aux = list_sort
                while idx+1 < len(list_aux):
                    if list_sort[idx][0] == list_sort[idx+1][0] and list_sort[idx][1] == list_sort[idx+1][1]:
                        list_sort.pop(idx+1)
                    if list_sort[idx][0] == list_sort[idx+1][0] and list_sort[idx][1] != list_sort[idx+1][1]:
                        list_sort[idx][0] += DELTA
                    idx += 1
                list_final = sorted(list_sort)
                print(list_final)
                for _ in list_final:
                        self.note.append(XyloNote(_[1],_[0],VELOCITY))
            else:
                raise ValueError('type must be either 1 or 2')

    def get_note(self):
        #returns a list of all instances of note
        return self.note


    

    

    
    