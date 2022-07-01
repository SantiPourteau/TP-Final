from __future__ import annotations
from scipy.io.wavfile import write


class Synthesizer():
    #server with the wav file
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,waveform,frequency):
        #accessed only one with the final waveform
        write(self.output_file,frequency,waveform) #write in wave file
        
        