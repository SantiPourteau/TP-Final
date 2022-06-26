from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin



class Wave():
    def __init__(self,note):
        self.note=note
        self.waveform=None
  
    def get_waveform(self,instrument,A:int):
        start=float(self.note.get_time()) 
        stop=float(self.note.get_time()+self.note.get_duration())
        step=0.001
        self.time=np.arange(start,stop,step)

        amp=float(instrument.get_harmonic_amplitude()[1])
        n_arm=int(instrument.get_harmonic_amplitude()[0])
        f=float(self.note.get_frequency())
        st=float(self.note.get_time())

        wave = A * amp * np.sin(2 * np.pi * f * n_arm * (self.time-st))
        self.waveform = np.int16(wave)
        return self.waveform

    def plot(self):
        return plt.plot(self.waveform,color="black")

    def case_wave(self,intrument):
        pass
    


