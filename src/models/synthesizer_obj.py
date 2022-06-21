class Synthesizer():
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,envolvente):
        #envolvente pasado a numpy array
        #falta muestrear la envolvente con la freq de muestreo (con array.arange creo)
        self.output_file.load(envolvente)
        self.output_file.save()
        
        