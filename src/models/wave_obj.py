from __future__ import annotations
import numpy as np
from functions import translate_functions
from src.models.instrument_obj import Instrument, get_attack


class Wave():
    def __init__(self, note):
        self.note = note
        self.waveform = None

    def get_waveform(self,frequency,instrument):
        # Samples per second
        sps = frequency  

        # Frequency / pitch of the sine wave
        freq_hz = float(self.note.get_frequency())

        # Duration
        duration_s = float(self.note.get_duration())

        #start time
        st=float(self.note.get_time())

        # NumpPy magic
        each_sample_number = np.arange(st*sps,st+duration_s * sps) 


        waveform=0

        for i in range(instrument.get_num_harmonics()): #addition of harmonics
            #amp harmonic
            m=float(instrument.get_respective_amplitude(i))

            waveform += i * np.sin(2 * np.pi * m * (each_sample_number-st) * freq_hz / sps)
        
        waveform_quiet = waveform * 0.3 #contant A
        self.waveform = np.int16(waveform_quiet * 32767) 
        return self.waveform

    def case_wave(self, at , dt , frequency , instrument: Instrument):
        #aca hacer el casing. es decir multiplicar waveform x funcion muduladora x A (constante de volumen del instrumento)
        #aca vamos a tener que implementar un diccionario con todos los posibles moduladores y sus funciones
        #https://scialicia.com/2018/08/python-frequency-modulation-with-numpy/

        sps = frequency
        att_time_x = (instrument.get_attack()[1][0])*sps
        dec_time_x = (instrument.get_decay()[1][0])*sps
        att, att_parameters = instrument.get_attack()
        sust, sust_parameters = instrument.get_sustain()
        dec, dec_parameters = instrument.get_decay

        for i in range(self.waveform):
            if i > 0 and i <= att_time_x:
                self.waveform[i] = self.waveform[i]*(translate_functions(att, att_parameters, i))
            if i > att_time_x and i < dec_time_x:
                self.waveform[i] = self.waveform[i]*(translate_functions(sust, sust_parameters, i))
            if i >= dec_time_x:
                self.waveform[i] = self.waveform[i]*(translate_functions(dec, dec_parameters, i))
        return self.waveform



