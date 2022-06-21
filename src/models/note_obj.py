from notes_mapping import notes_mapping_dict

class Note():
    def __init__(self,nota):
        self.frecuencia = notes_mapping_dict[nota]
    
    def get_frecuencia(self):
        return self.frecuencia
    

