import argparse
from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
from xylophone.server.server import XyloServer
from xylophone.server.server import MockXyloServer

def interactuar(partitura,dispositivo=None):
    notes = filtrar_partitura(partitura)
    client = XyloClient(host='localhost', port=8080) #esta bien que tire connection refused
    client.load(notes)
    client.play()

def filtrar_partitura(partitura):
    accepted_notes = ['C7','C#7','Cb7','B6','Bb6','A6','A#6','Ab6','G6','G#6','Gb6','F6','F#6','E6','Eb6','D6','D#6','Db6','C6','C#6','B5','Bb5','A5','A#5','Ab5','G5','F5','E5','Eb5','D5','D#5','Db5','C5','C#5','B4','Bb4','A4','A#4','Ab4','G4','G#4']
    list = []
    notes=[]
    with open(partitura,"r") as f:
        for line in f:
            line = line.strip('\n').split(' ')
            if line[1] in accepted_notes:
                list.append([int(line[0]),line[1]])
    list_sort = sorted(list)
    idx = 0
    while idx+1 < len(list):
        if list_sort[idx][0] == list_sort[idx+1][0]:
            list_sort[idx][0] += 0.00001
        idx += 1
    list_final = sorted(list_sort)
    for _ in list_final:
            notes.append(XyloNote(_[1],_[0],90))
    return notes

def main() -> None:
    parser = argparse.ArgumentParser(description='metalofone')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-d', '--dispositivo', help='dispositivo')
    
    arg = parser.parse_args()

    interactuar(arg.partitura, arg.dispositivo)

if __name__ == '__main__':
    interactuar('partitura.txt')
    main()


    