from __future__ import annotations
from models.wave_obj import Wave
import scipy

class Synthesizer():
    def __init__(self,output_file):
        self.output_file=output_file

    def synthesize(self,wave:Wave,frequency):
        scipy.io.wavfile.write(self.output_file,frequency,wave.get_np_array())
        
        