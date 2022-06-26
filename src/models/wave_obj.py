from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin
from models.instrument_obj import Instrument


class Wave():
    def __init__(self,note):
        self.note=note
        self.fn=None

    def get_np_array(self,instrument:Instrument,A:int):
        time_array=np.arange(self.note.time(),self.note.get_time()+self.note.get_duration(),0.001)
        freq_list=[]
        for time in time_array:
            freq=self.A * self.instrument.get_harmonic_amplitude()[1] *sin(2*pi*self.note.get_frequency()*self.instrument.get_harmonic_amplitude()[0]*(time-self.note.get_time()))
            freq_list.append(freq)
        freq_array=np.array(freq_list)
        self.fn=np.array(time_array,freq_array)
        return self.fn

    def plot(self):
        return plt.plot(self.fn[0],self.fn[1],color="black")

    def case_wave(self,intrument:Instrument):
        pass
    


