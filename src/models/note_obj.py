from src.notes_mapping import notes_mapping_dict
import src.models.wave_obj

class Note():
    def __init__(self,time,note,duration):
        """
        Class for musical notes

        args:
        time = start time of note
        frequency = frequency of note
        duration = duration of note
        """
        self.time=time
        self.frequency=notes_mapping_dict[note] #gets the freq of note from dictionary of notes
        self.duration=duration

    def get_frequency(self):
        return self.frequency

    def get_time(self):
        return self.time

    def get_duration(self):
        return self.duration
    
    def get_wave(self):
        #instance of wave created
        return src.models.wave_obj.Wave(self)
    
    

