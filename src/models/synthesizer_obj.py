from __future__ import annotations
import time
from scipy.io.wavfile import write
import sounddevice as sd

class Synthesizer():
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,waveform,frequency):
        write(self.output_file,frequency,waveform)
        #analisar despues si esta appendding o overwriting
        
        