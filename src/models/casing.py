from math import pi, sin
import numpy as np
from wave_obj import Wave


class Casing():
    def __init__(self,instrument,A,frequency):
        self.A=A
        self.instrument=instrument
        self.frequency=frequency
        self.case=None
    
    def case(self,note):
        time_array=np.arange(note.time(),note.get_time()+note.get_duration(),note.get_duration()/self.frequency)
        freq_list=[]
        for time in time_array:
            freq=self.A * self.instrument.get_harmonic_amplitude()[1] *sin(2*pi*note.get_frequency()*self.instrument.get_harmonic_amplitude()[0]*(time-note.get_time()))
            freq_list.append(freq)
        freq_array=np.array(freq_list)
        
        self.case=np.array(time_array,freq_array)


    def get_wave(self):
        return Wave(self.case)
        