import argparse
from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
from xylophone.server.server import XyloServer
from xylophone.server.server import MockXyloServer

def interactuar(partitura,dispositivo=None):
    notes=[]
    with open(partitura,"r") as f:
        for line in f:
            line = line.strip('\n').split(' ')
            notes.append(XyloNote(line[1],line[0],90))
    client = XyloClient(host='localhost', port=8080)
    client.load(notes)
    client.play()


def main() -> None:
    parser = argparse.ArgumentParser(description='metalofone')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-d', '--dispositivo', help='dispositivo')
    
    arg = parser.parse_args()

    interactuar(arg.partitura, arg.dispositivo)

if __name__ == '__main__':
    interactuar('partitura.txt')
    main()


    