from math import pi, sin

from onda_obj import Onda


class Envolvente():
    def __init__(self,instrumento,A):
        self.instrumento=instrumento
        self.A=A
    
    def envolver(self,partitura,instrumento):
        def f(t):
            return self.A * instrumento.get_armonico_amplitud()[1] *sin(2*pi*partitura.get_frecuencia()*instrumento.get_armonico_amplitud()[0]*(t-partitura.get_time()))

        return Onda(f)
        