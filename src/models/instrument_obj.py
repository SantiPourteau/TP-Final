
import os
class Instrument():
    def __init__(self, txt_instrument):
        """
        Class for keeping all instrument information received

        args:
        txt_instrument: txt file that contains information for the instrument
        """
        with open (txt_instrument,"r") as f:
            if os.path. getsize(txt_instrument) == 0:
                raise SystemExit()

            else:

                self.amplitude=[]
                counter=0
                for line in f: #iterates over text file
                    if counter==0:

                        self.num_harmonics=int(line.split()[0]) #num harmonics

                    if counter!=0 and counter<=self.num_harmonics:
                        self.amplitude.append(line.split()[1]) #amplitude corresponding to each harmonic
                    
                    #attack params
                    if counter==self.num_harmonics+1: #parameters vary from 0 to 3 so managing errors with try/except
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
                    #sustain params
                    if counter==self.num_harmonics+2: #parameters vary from 0 to 3 so managing errors with try/except
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
                    #decay params   
                    if counter==self.num_harmonics+3: #parameters vary from 0 to 3 so managing errors with try/except
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
        #get the multiplier of a specific harmonic
        try:
            return self.amplitude[n_of_harmonic-1] #-1 as [0] is for harmonic number 1
        except IndexError:
            return f"The instrument has only {self.get_num_harmonics} harmonics"
  
    def get_attack(self):
        return [self.attack,self.attack_parameters] 
    
    def get_sustain(self):
        return [self.sustain,self.sustain_parameters]
    
    def get_decay(self):
        return [self.decay,self.decay_parameters]



        