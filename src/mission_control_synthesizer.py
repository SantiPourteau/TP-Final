import argparse

from models.instrument_obj import Instrument
from models.music_sheet_obj import Music_Sheet
from models.synthesizer_obj import Synthesizer

A=20 #constante que le da el volumen al instrumento ?!

def sintetizar(A,frequency, instrument_txt, music_sheet_txt, output):
    instrument=Instrument(instrument_txt)
    music_sheet=Music_Sheet(music_sheet_txt)
    synthesizer=Synthesizer(output)

    note= music_sheet.get_note()
    wave=note.get_wave()
    wave.get_np_array(instrument,A)
    wave.plot()
    synthesizer.synthesize(wave,frequency)


    


def main() -> None:
    parser = argparse.ArgumentParser(description='sintetizador')
    parser.add_argument('-f', '--frecuencia', help='frecuencia')
    parser.add_argument('-i', '--instrumento', help='instrumento')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-o', '--output', help='audio.wav')

    arg = parser.parse_args()

    sintetizar(arg.frecuencia, arg.instrumento, arg.partitura, arg.output)

if __name__ == '__main__':
    sintetizar(20,440,"instrument.txt","partitura.txt","output.wav")


    main()


    