class Sintetizador():
    def __init__(self,output_file):
        self.output_file=output_file

    def sintetizar(self,envolvente):
        self.output_file.load(envolvente)
        self.output_file.save()
        
        