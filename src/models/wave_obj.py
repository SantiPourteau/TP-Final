from __future__ import annotations
import numpy as np


class Wave():
    #manages the waveform of the note
    def __init__(self, note):
        self.note = note
        self.waveform = None

    def get_waveform(self,frequency,instrument):
        sps = frequency  # Samples per second
        freq_hz = float(self.note.get_frequency()) # Frequency / pitch of the sine wave
        duration_s = float(self.note.get_duration()) # Duration
        st=float(self.note.get_time()) #start time
        each_sample_number = np.arange(st*sps,(st*sps+duration_s * sps)) # the time axis

        waveform=0
        for i in range(instrument.get_num_harmonics()): #addition of harmonics
            
            m=float(instrument.get_respective_amplitude(i)) #amp harmonic (multiplier)

            waveform += m * np.sin(2 * np.pi * i * (each_sample_number-st) * freq_hz / sps) #wave equation with numpy
        
            self.waveform=waveform

        return self.waveform

    def case_wave(self,intrument):
        #modify self.waveform when casing
        return self.waveform
    


