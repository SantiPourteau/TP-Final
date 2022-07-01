import argparse
from models.music_sheet_obj import Music_Sheet
from src.xylophone.xylophone.client import XyloClient
from src.xylophone.xylophone.xylo import XyloNote
from src.xylophone.xylophone.server.server import XyloServer
from src.xylophone.xylophone.server.server import MockXyloServer



def interact(music_sheet,device=None):
    """
    Interacts with a device

    args:
        - sheet: Music sheet with start time, note and duration
        - device
    """
    sheet = Music_Sheet(music_sheet)
    client = XyloClient(host='10.42.0.1', port=8080) #esta bien que tire connection refused
    print(sheet.filter_notes_metalofon(sheet))
    client.load(sheet.filter_notes_metalofon(sheet))
    client.play()

def main() -> None:
    parser = argparse.ArgumentParser(description='metalofone')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-d', '--dispositivo', help='dispositivo')
    
    arg = parser.parse_args()

    interact(arg.partitura, arg.dispositivo)

if __name__ == '__main__':
    interact()
    main()
    


    