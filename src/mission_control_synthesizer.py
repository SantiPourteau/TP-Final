import argparse

from models.instrument_obj import Instrument
from models.music_sheet_obj import Music_Sheet
from models.synthesizer_obj import Synthesizer



def sintetizar(frequency, instrument_txt, music_sheet_txt, output):
    #aca creamos las instancias de los objetos
    instrument=Instrument(instrument_txt)
    music_sheet=Music_Sheet(music_sheet_txt)
    synthesizer=Synthesizer(output)

#esto va a ser un loop para cada nota de la partitura.
    note= music_sheet.get_note() #aca se crea la instancia de nota
    wave=note.get_wave() #aca se crea la instancia de wave
    waveform=wave.get_waveform(frequency,instrument) #conseguimos el np array correspondiente
    #aca falta case la wave q es lo q finalmente se sintetiza -> wave.case()
    synthesizer.synthesize(waveform,frequency) # lo escribimos en el wave file

def main() -> None:
    parser = argparse.ArgumentParser(description='sintetizador')
    parser.add_argument('-f', '--frecuencia', help='frecuencia')
    parser.add_argument('-i', '--instrumento', help='instrumento')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-o', '--output', help='audio.wav')

    arg = parser.parse_args()

    sintetizar(arg.frecuencia, arg.instrumento, arg.partitura, arg.output)

if __name__ == '__main__':
    sintetizar(44100,"instrument.txt","partitura.txt","output.wav")


    # main()


    