class Sintetizador():
    def __init__(self,output_file):
        self.output_file=output_file

    def sintetizar(self,envolvente):
        #falta muestrear la envolvente con la freq de muestreo
        #aca me imagino que hay q usar numpy para hacer el load a wav file
        self.output_file.load(envolvente)
        self.output_file.save()
        
        