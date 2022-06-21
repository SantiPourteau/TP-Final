from notes_mapping import notes_mapping_dict

class Note():
    def __init__(self,nota):
        self.frequency = notes_mapping_dict[nota]
    
    def get_frequency(self):
        return self.frequency
    

