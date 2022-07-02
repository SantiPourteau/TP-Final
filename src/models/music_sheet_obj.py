from notes_mapping import notes_mapping_dict

DELTA = 0.00001
VELOCITY = 90
class Music_Sheet():
    #music sheet keep music sheet information
    def __init__(self, txt_sheet,type):
        """
        txt_sheet: A txt file that contains the information for the Music Sheet
        type: The type defines which type of information will be processed, 1 will process the information for the 
              synthesizer and 2 will process the information for the xylophone
        """
        self.notes=[]
        self.type = type
        with open(txt_sheet) as f: 
            data=[]
            for line in f:
                data.append(line.split()) #list of lists created
                if line.split()[1] not in notes_mapping_dict:
                    raise ValueError("Note not supported by sinthesizer")

            data=sorted(data,key=lambda inner_list: int(inner_list[0])) #sorted based on start time
            if self.type == 1:
                import models.note_obj
                """
                Filters the data from the Music Sheet to be used by the sinthesizer
                """
                counter = 0
                for elem in data: #iteration over data to create instances of note object
                    if counter==0: 
                        if elem[0] == 0:
                            time,note,duration=elem[0],elem[1],elem[2]
                            self.notes.append(models.note_obj.Note(time,note,duration))
                        else:
                            #generate a note for inicial silence
                            time,note,duration=0,"None",elem[0]
                            self.notes.append(models.note_obj.Note(time,note,duration))
                            #note after silence
                            time,note,duration=elem[0],elem[1],elem[2]
                            self.notes.append(models.note_obj.Note(time,note,duration)) 
                    if counter>0:
                        if elem[0]==time+duration:                     
                            time,note,duration=elem[0],elem[1],elem[2]
                            self.notes.append(models.note_obj.Note(time,note,duration))
                        else:
                            #generate a note for silence moments
                            time=float(time)+float(duration)
                            note="None"
                            duration=abs(float(time)-int(elem[0]))
                            self.notes.append(models.note_obj.Note(time,note,duration))
                            
                            #generate note after silence
                            time,note,duration=elem[0],elem[1],elem[2]
                            self.notes.append(models.note_obj.Note(time,note,duration))

                    counter+=1
            elif self.type == 2:
                from xylophone.xylophone.xylo.note import XyloNote
                """
                Filters the data from the Music Sheet to be used by the Xylophone
                """
                accepted_notes = ['C7','C#7','Cb7','B6','Bb6','A6','A#6','Ab6','G6','G#6','Gb6','F6','F#6','E6','Eb6','D6','D#6','Db6','C6','C#6','B5','Bb5','A5','A#5','Ab5','G5','F5','E5','Eb5','D5','D#5','Db5','C5','C#5','B4','Bb4','A4','A#4','Ab4','G4','G#4']
                list = []
                for _ in data:
                    if _[1] in accepted_notes: #checks if the xylophone can play the note
                        list.append([int(_[0]),_[1]])
                    if _[1] not in accepted_notes:
                        raise ValueError(f'{_[1]} is not in accepted notes')
                idx = 0
                list_aux = list
                while idx+1 < len(list_aux): #filters the notes 
                    if list[idx][0] == list[idx+1][0] and list[idx][1] == list[idx+1][1]: #if the same note is played at the same time, one of the instances is deleted, 
                        list.pop(idx+1)
                    if list[idx][0] == list[idx+1][0] and list[idx][1] != list[idx+1][1]: #if different notes are played at the same time, one of the notes is moved by DELTA
                        list[idx][0] += DELTA
                    idx += 1
                list_final = sorted(list)
                for _ in list_final: #creates instances of XyloNote for the notes in the Music Sheet
                        self.notes.append(XyloNote(_[1],_[0],VELOCITY))
            else:
                raise ValueError('type must be either 1 or 2')

    def get_note(self):
        #returns a list of all instances of note
        return self.notes


    

    

    
    