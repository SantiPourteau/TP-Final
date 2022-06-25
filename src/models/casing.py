from math import pi, sin
import numpy as np
from wave_obj import Wave


class Casing():
    def __init__(self,instrument,A,frequency):
        self.A=A
        self.instrument=instrument
        self.frequency=frequency
        self.case=np.empty()
    
    def case(self,note):
        #hacerle todo para q array con los valores que toma la funcion de abajo....
        #tener en cuenta el muestro /freq
        """
        f(t)=self.A * self.instrument.get_harmonic_amplitude()[1] *sin(2*pi*note.get_frequency()*self.instrument.get_harmonic_amplitude()[0]*(t-note.get_time()))

        for t in range(muestreo)
            append a self.case [t,f(t)]

        algo asi creo ajajaj
        """
        self.case
        return 
        
    
    def get_wave(self):
        return Wave(self.case)
        