from notes_mapping import notes_mapping_dict
import models.wave_obj

class Note():
    def __init__(self,time,nota,duration):
        self.time=time
        self.frequency=notes_mapping_dict[nota]
        self.duration=duration

    def get_frequency(self):
        return self.frequency
    def get_time(self):
        return self.time
    def get_duration(self):
        return self.duration
    
    def get_wave(self):
        return models.wave_obj.Wave(self)
    
    

