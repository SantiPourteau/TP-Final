import argparse
from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
from xylophone.server.server import XyloServer


def interactuar(partitura,dispositivo):
    server=XyloServer()
    server.start()
    client=XyloClient()
    notes=[]
    with open(partitura,"r") as f:
        for line in f:
            notes.append(XyloNote(line[1],line[0],90))
    client.load(notes)
    client.play()


def main() -> None:
    parser = argparse.ArgumentParser(description='metalofon')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-d', '--dispositivo', help='dispositivo')
    
    arg = parser.parse_args()

    interactuar(arg.partitura, arg.dispositivo)

if __name__ == '__main__':
    main()


    