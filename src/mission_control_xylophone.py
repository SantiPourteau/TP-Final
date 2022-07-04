import argparse
from src.models.music_sheet_obj import Music_Sheet
from src.xylophone.client import XyloClient
from src.models.device_obj import Device
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
    if len(music_sheet.get_note()) == 0:
        print('There are no notes in the file received')
        raise SystemExit()
    print('Loading Client...')
    client = XyloClient(device.get_host(),device.get_port()) 
    client.load(sheet.get_note())
    client.play()

def main() -> None:
    parser = argparse.ArgumentParser(description='xylophone')
    parser.add_argument('-p', '--music_sheet', help='Music_Sheet that will be interpreted')
    parser.add_argument('-d', '--device', help='Device that computer will connect to')
    
    arg = parser.parse_args()

    interact(arg.music_sheet, arg.device)

if __name__ == '__main__':
    main()
    


    