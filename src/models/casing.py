from math import pi, sin

from wave_obj import Wave


class Casing():
    def __init__(self,instrument,A):
        self.instrument=instrument
        self.A=A
    
    def case(self,note,instrument):
        def f(t):
            #todo esto pero en arrays!!!
            return self.A * instrument.get_harmonic_amplitude()[1] *sin(2*pi*note.get_frequency()*instrument.get_harmonic_amplitude()[0]*(t-note.get_time()))
    
        return Wave(f)
        