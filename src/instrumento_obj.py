class Instrument():
    def __init__(self, txt_instrumento):
        with open (txt_instrumento) as f:
            contador=0
            for line in f:
                if contador==0:
                    self.nro_armonicos=int(line.split()[0])
        
                if contador!=0 and contador<=self.nro_armonicos:
                    self.armonico=line.split()[0]
                    self.amplitud=line.split()[1]
                
                if contador==self.nro_armonicos+1:
                    self.ataque=line.split()[0]
                    self.ataque_parametro=line.split()[1]
                
                if contador==self.nro_armonicos+2:
                    self.sustain=line.split()[0]
                    try:
                        self.sustain_parametro=line.split()[1]
                    except IndexError:
                        self.sustain_parametro=None
                
                if contador==self.nro_armonicos+3:
                    self.decay=line.split()[0]
                    self.decay_parametro=line.split()[1]

                contador+=1


    def get_armonico_amplitud(self):
        return [self.armonico,self.amplitud]
  
    def get_ataque(self):
        return [self.ataque,self.ataque_parametro]
    
    def get_sustain(self):
        return [self.sustain,self.sustain_parametro]
    
    def get_decay(self):
        return [self.decay,self.decay_parametro]

        
    
        
