from __future__ import annotations
import time
from scipy.io.wavfile import write
import sounddevice as sd

class Synthesizer():
    #server que va a conservar el wave file
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,waveform,frequency):
        #aca es donde trabajamos con el array sobre el wave file
        write(self.output_file,frequency,waveform)
        #analisar despues si esta appendding o overwriting
        
        