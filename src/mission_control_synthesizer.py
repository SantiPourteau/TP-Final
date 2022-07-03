import argparse
import numpy as np
from models.instrument_obj import Instrument
from models.music_sheet_obj import Music_Sheet
from models.synthesizer_obj import Synthesizer



def sintetizar(frequency, instrument_txt, music_sheet_txt, output):
    
    #object instances created
    instrument=Instrument(instrument_txt)
    music_sheet=Music_Sheet(music_sheet_txt,1)
    synthesizer=Synthesizer(output)

    contador=0
    for note in music_sheet.get_note(): #loop for each note already sorted and including silence notes
        wave=note.get_wave() #instance of wave created
        waveform=wave.get_waveform(frequency,instrument) #get waveform
        waveform=wave.case_wave(instrument,frequency) #case that same waveform
        if contador==0:
            waveform1=waveform
        if contador>0:
            waveform1=np.append(waveform1,waveform) #appending notes in one same waveform
        contador+=1
        
    waveform_quiet = waveform1 * 0.3 #contant A to manage instrument volume (base tenia 0.3 y probe con mas chico y va mejor creo)
    waveform = np.int16(waveform_quiet * 32767) #scaling amplitude (omiting this would round all amps to 0 when written in wav file)

    synthesizer.synthesize(waveform,frequency) #write in wave file through synthesizer

def main() -> None:
    parser = argparse.ArgumentParser(description='sintetizador')
    parser.add_argument('-f', '--frecuencia', help='frecuencia')
    parser.add_argument('-i', '--instrumento', help='instrumento')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-o', '--output', help='audio.wav')

    arg = parser.parse_args()

    sintetizar(arg.frecuencia, arg.instrumento, arg.partitura, arg.output)

if __name__ == '__main__':
    sintetizar(44100,"piano.txt","queen.txt","output.wav") #testing function


    # main() #for running with parser arguments


    