class Synthesizer():
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,onda):
        
        self.output_file.load(onda)
        #el load y eso hacerlo con scikit-sound 
        self.output_file.save()
        
        