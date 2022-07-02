import argparse
from models.music_sheet_obj import Music_Sheet
from xylophone.xylophone.client import XyloClient
from xylophone.xylophone.xylo import XyloNote

def interact(music_sheet,device=None):
    """
    Interacts with a device

    args:
        - sheet: Music sheet with start time, note and duration
        - device
    """
    sheet = Music_Sheet(music_sheet,2)
    client = XyloClient(host='10.42.0.1', port=8080) #esta bien que tire connection refused
    client.load(sheet.get_note())
    client.play()

def main() -> None:
    parser = argparse.ArgumentParser(description='metalofone')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-d', '--dispositivo', help='dispositivo')
    
    arg = parser.parse_args()

    interact(arg.partitura, arg.dispositivo)

if __name__ == '__main__':
    interact('partitura.txt')
    main()
    


    