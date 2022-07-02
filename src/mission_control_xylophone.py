import argparse
from models.music_sheet_obj import Music_Sheet
from xylophone.xylophone.client import XyloClient
from models.device_obj import Device
HOST = '10.42.0.1'
PORT = 8080
def interact(music_sheet,device):
    """
    Interacts with a device

    args:
        - sheet: Music sheet with start time, note and duration
        - device: device which the computer will connect to, the port and host-ip are hard-coded beforehand.
    """
    device = Device(device,HOST,PORT)
    sheet = Music_Sheet(music_sheet,2)
    client = XyloClient(device.get_host(),device.get_port()) 
    client.load(sheet.get_note())
    client.play()

def main() -> None:
    parser = argparse.ArgumentParser(description='xylophone')
    parser.add_argument('-p', '--sheet', help='Music_Sheet that will be interpreted my Xylophone')
    parser.add_argument('-d', '--device', help='Device that computer will connect to')
    
    arg = parser.parse_args()

    interact(arg.sheet, arg.device)

if __name__ == '__main__':
    interact('partitura.txt','kitty')
    main()
    


    