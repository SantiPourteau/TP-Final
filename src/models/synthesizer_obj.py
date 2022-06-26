from __future__ import annotations
from models.wave_obj import Wave
from scipy.io.wavfile import write

class Synthesizer():
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,waveform,frequency):
        write(self.output_file,frequency,waveform)
        
        