class Synthesizer():
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,envolvente):
        #falta muestrear la envolvente con la freq de muestreo (con array.arange creo)
        self.output_file.load(envolvente)
        #el load y eso hacerlo con scikit-sound 
        self.output_file.save()
        
        