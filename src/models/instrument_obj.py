
class Instrument():
    #keeps all instrument information
    def __init__(self, txt_instrumento):
        with open (txt_instrumento,"r") as f:
            self.amplitude=[]
            counter=0
            for line in f:
                if counter==0:
                    self.num_harmonics=int(line.split()[0])
        
                if counter!=0 and counter<=self.num_harmonics:
                    self.amplitude.append(line.split()[1])
                
                if counter==self.num_harmonics+1:
                    self.attack=line.split()[0]
                    self.attack_parameters=[]
                    try:
                        self.attack_parameters.append(float(line.split()[1]))
                    except IndexError:
                        pass
                    try:
                        self.attack_parameters.append(float(line.split()[2]))
                    except IndexError:
                        pass
                    try:
                        self.attack_parameters.append(float(line.split()[3]))
                    except IndexError:
                        pass
 
                if counter==self.num_harmonics+2:
                    self.sustain=line.split()[0]
                    self.sustain_parameters=[]
                    try:
                        self.sustain_parameters.append(float(line.split()[1]))
                    except IndexError:
                        pass
                    try:
                        self.sustain_parameters.append(float(line.split()[2]))
                    except IndexError:
                        pass
                    try:
                        self.sustain_parameters.append(float(line.split()[2]))
                    except IndexError:
                        pass
                    
                if counter==self.num_harmonics+3:
                    self.decay=line.split()[0]
                    self.decay_parameters=[]
                    try:
                        self.decay_parameters.append(float(line.split()[1]))
                    except IndexError:
                        pass
                    try:
                        self.decay_parameters.append(float(line.split()[2]))
                    except IndexError:
                        pass
                    try:
                        self.decay_parameters.append(float(line.split()[3]))
                    except IndexError:
                        pass

                counter+=1

    def get_num_harmonics(self):
        return self.num_harmonics

    def get_respective_amplitude(self,n_of_harmonic):
        try:
            return self.amplitude[n_of_harmonic-1]
        except IndexError:
            return f"The instrument has only {self.get_num_harmonics} harmonics"
  
    def get_attack(self):
        return [self.attack,self.attack_parameters] 
    
    def get_sustain(self):
        return [self.sustain,self.sustain_parameters]
    
    def get_decay(self):
        return [self.decay,self.decay_parameters]



        