from notes_mapping import notes_mapping_dict

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
    

