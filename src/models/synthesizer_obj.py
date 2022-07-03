from __future__ import annotations
from scipy.io.wavfile import write


class Synthesizer():
    #server with the wav file
    def __init__(self,output_file):
        """
        Class that creates the synthesizer object 

        args:
            - output_file: name of output_file to be created or if it exists to overwrite
        """
        self.output_file=output_file

    def synthesize(self,waveform,frequency):
        """
        Function that writes the final waveform in wavefile

        args:
            - waveform: final waveform
            -frequency
        """
        #accessed only one with the final waveform
        write(self.output_file,frequency,waveform) #write in wave file
        
        