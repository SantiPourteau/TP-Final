from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np


class Wave():
    #aca vamos a laburar la forma de la onda. y es donde conseguimos el np array que
    #...despues vamos a subir al wave file
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
        
        waveform_quiet = waveform * 0.3 #investigar esta multiplicacion
        self.waveform = np.int16(waveform_quiet * 32767) #investigar esta multiplicacion
        return self.waveform

    def case_wave(self,intrument):
        #aca hacer el casing. es decir multiplicar waveform x funcion muduladora x A (constante de volumen del instrumento)
        #aca vamos a tener que implementar un diccionario con todos los posibles moduladores y sus funciones
        #https://scialicia.com/2018/08/python-frequency-modulation-with-numpy/
        pass
    


