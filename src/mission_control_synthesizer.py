import argparse

from src.models.casing import Casing
from src.models.instrument_obj import Instrument
from src.models.music_sheet_obj import Music_Sheet
from src.models.synthesizer_obj import Synthesizer

A=20 #constante que le da el volumen al instrumento ?!

def sintetizar(A,frequency, instrument_txt, music_sheet_txt, output):
    instrument=Instrument(instrument_txt)
    music_sheet=Music_Sheet(music_sheet_txt)
    casing=Casing(instrument,A,frequency)
    synthesizer=Synthesizer(output)

    #arrancar a interactuar con los objetos...


def main() -> None:
    parser = argparse.ArgumentParser(description='sintetizador')
    parser.add_argument('-f', '--frecuencia', help='frecuencia')
    parser.add_argument('-i', '--instrumento', help='instrumento')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-o', '--output', help='audio.wav')

    arg = parser.parse_args()

    sintetizar(arg.frecuencia, arg.instrumento, arg.partitura, arg.output)

if __name__ == '__main__':
    main()


    