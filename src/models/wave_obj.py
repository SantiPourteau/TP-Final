from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin



class Wave():
    def __init__(self,note):
        self.note=note
        self.time=[]
        self.freq=[]

    def get_np_array(self,instrument,A:int):
        start=float(self.note.get_time()) 
        stop=float(self.note.get_time()+self.note.get_duration())
        step=0.001
        self.time=np.arange(start,stop,step)
        
        for time in self.time:
            amp=float(instrument.get_harmonic_amplitude()[1])
            n_arm=int(instrument.get_harmonic_amplitude()[0])
            f=float(self.note.get_frequency())
            st=float(self.note.get_time())
            time=float(time)
            freq=A*amp*sin(2*pi*f*n_arm*(time-st))
            self.freq.append(freq)
        return np.array(tuple(self.time),tuple(self.freq))

    def plot(self):
        return plt.plot(self.time,self.freq,color="black")

    def case_wave(self,intrument):
        pass
    


