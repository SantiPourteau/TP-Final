from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np


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

        #harmonic
        i=float(instrument.get_harmonic_amplitude()[0])

        #amp harmonic
        m=float(instrument.get_harmonic_amplitude()[1])

        #start time
        st=float(self.note.get_time())

        # NumpPy magic
        each_sample_number = np.arange(duration_s * sps)
        waveform = i * np.sin(2 * np.pi * m * (each_sample_number-st) * freq_hz / sps)
        #esta funcion va a ser sumatoria cuando tengamos mas harmonicos...el i y el m va a variar en un for loop
        waveform_quiet = waveform * 0.3 
        self.waveform = np.int16(waveform_quiet * 32767)
        #esto ultimo lo saque de internet asi q no pregunten
        return self.waveform

    def case_wave(self,intrument):
        #aca hacer el casing. es decir multiplicar waveform x funcion muduladora x A (constante de volumen del instrumento)
        #aca vamos a tener que implementar un diccionario con todos los posibles moduladores y sus funciones
        #https://scialicia.com/2018/08/python-frequency-modulation-with-numpy/
        pass
    


