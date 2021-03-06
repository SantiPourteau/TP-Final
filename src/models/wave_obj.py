from __future__ import annotations
import numpy as np
from src.models.functions import translate_functions


class Wave():
    def __init__(self, note):
        """
        Class for waves

        args:
            note: Note object
        """
        self.note = note
        self.waveform = None

    def get_waveform(self,frequency,instrument):
        """
        Function that gets the waveform for a specific frequency and the instrument

        args:
            - frequency: sample rate
            - instrument: instance of Instrument Object
        """
        sps = frequency  # Samples per second
        freq_hz = float(self.note.get_frequency()) # Frequency / pitch of the sine wave
        duration_s = float(self.note.get_duration()) # Duration
        st=float(self.note.get_time()) #start time
        each_sample_number = np.arange(st*sps,(st*sps+duration_s * sps)) # x values array
        if self.note.get_frequency()==0:
            shape = len(each_sample_number)
            self.waveform=np.zeros(shape)
            return self.waveform
        
        waveform=0
        for i in range(1,instrument.get_num_harmonics()+1): #addition of harmonics
            m=float(instrument.get_respective_amplitude(i))#amp harmonic / multiplier

            waveform += m * np.sin(2 * np.pi * i * (each_sample_number) * freq_hz / sps)
        self.waveform=waveform
        return self.waveform

    def case_wave(self, instrument,frequency):
        """
        Modifies the Attack, Sustain and Decay parts of the wave

        args:
            - instrument: instance of Instrument Object
            - frequency: Sample Rate
        """
        if self.note.get_frequency() == 0:
            return self.waveform

        sps = frequency
        att_time = (instrument.get_attack()[1][0])*sps
        dec_time = (instrument.get_decay()[1][0])*sps
        
        att_type, att_parameters = instrument.get_attack() 
        sust_type, sust_parameters = instrument.get_sustain()
        dec_type, dec_parameters = instrument.get_decay()

        for i in range(len(self.waveform)):
            if i > 0 and i <= att_time:
                self.waveform[i] = self.waveform[i]*(translate_functions(att_type, att_parameters, i, sps))
            if i > att_time and i < ((len(self.waveform))-dec_time):
                self.waveform[i] = self.waveform[i]*(translate_functions(sust_type, sust_parameters, i, sps))
            if i >= ((len(self.waveform))-dec_time):
                self.waveform[i] = self.waveform[i]*(translate_functions(dec_type, dec_parameters, i, sps))
        return self.waveform



