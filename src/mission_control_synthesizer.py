import argparse
import numpy as np
from models.instrument_obj import Instrument
from models.music_sheet_obj import Music_Sheet
from models.synthesizer_obj import Synthesizer



def sintetizar(frequency, instrument_txt, music_sheet_txt, output):
    #aca creamos las instancias de los objetos
    instrument=Instrument(instrument_txt)
    music_sheet=Music_Sheet(music_sheet_txt)
    synthesizer=Synthesizer(output)

    
#esto va a ser un loop para cada nota de la partitura.
    contador=0
    for note in music_sheet.get_note():
        wave=note.get_wave() #aca se crea la instancia de wave
        waveform=wave.get_waveform(frequency,instrument) #conseguimos el np array correspondiente
        #aca falta case la wave q es lo q finalmente se sintetiza -> wave.case()
        if contador==0:
            waveform1=waveform
        if contador>0:
            waveform1=np.append(waveform1,waveform)
        contador+=1
        
    waveform_quiet = waveform1 * 0.3 #contant A
    waveform = np.int16(waveform_quiet * 32767) 

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


    