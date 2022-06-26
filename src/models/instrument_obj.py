import os

class Instrument():
    def __init__(self, txt_instrumento):
        with open (txt_instrumento,"r") as f:
            counter=0
            for line in f:
                if counter==0:
                    self.num_harmonics=int(line.split()[0])
        
                if counter!=0 and counter<=self.num_harmonics:
                    self.harmonic=line.split()[0]
                    self.amplitude=line.split()[1]
                
                if counter==self.num_harmonics+1:
                    self.attack=line.split()[0]
                    self.attack_parameter=line.split()[1]
                
                if counter==self.num_harmonics+2:
                    self.sustain=line.split()[0]
                    try:
                        self.sustain_parameter=line.split()[1]
                    except IndexError:
                        self.sustain_parameter=None
                
                if counter==self.num_harmonics+3:
                    self.decay=line.split()[0]
                    self.decay_parameter=line.split()[1]

                counter+=1

    def get_harmonic_amplitude(self):
        return [self.harmonic,self.amplitude]
  
    def get_attack(self):
        return [self.attack,self.attack_parameter]
    
    def get_sustain(self):
        return [self.sustain,self.sustain_parameter]
    
    def get_decay(self):
        return [self.decay,self.decay_parameter]

        

        