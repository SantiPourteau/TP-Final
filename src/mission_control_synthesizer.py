import argparse
import numpy as np
from models.instrument_obj import Instrument
from models.music_sheet_obj import Music_Sheet
from models.synthesizer_obj import Synthesizer

A = 0.3

def sintetizar(frequency, instrument_txt, music_sheet_txt, output):
    
    #object instances created
    instrument=Instrument(instrument_txt)
    music_sheet=Music_Sheet(music_sheet_txt,1)
    synthesizer=Synthesizer(output)

    lastnote=music_sheet.get_note()[-1]
    shape=int(frequency*(float(lastnote.get_time())+float(lastnote.get_duration())))
    waveform_final=np.zeros(shape)
    
    
    for note in music_sheet.get_note(): #loop for each note already sorted and including silence notes
        wave=note.get_wave() #instance of wave created
        waveform=wave.get_waveform(frequency,instrument) #get waveform
        waveform=wave.case_wave(instrument,frequency) #case that same waveform
        
        startt=frequency*int(note.get_time())
        stopp=startt + frequency*int(note.get_duration())

        contador=0
        for i in range(startt,stopp):
            waveform_final[i]+=waveform[contador]
            contador+=1
        
    waveform_quiet = waveform_final * A #contant A to manage instrument volume (base tenia 0.3 y probe con mas chico y va mejor creo)
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
    sintetizar(44100,"instrument.txt","partitura.txt","output.wav") #testing function


    # main() #for running with parser arguments


    