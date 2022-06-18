import argparse
from metalofon import interactuar


def main() -> None:
    parser = argparse.ArgumentParser(description='metalofon')
    parser.add_argument('-p', '--partitura', help='partitura')
    parser.add_argument('-d', '--dispositivo', help='dispositivo')
    
    arg = parser.parse_args()

    interactuar(arg.partitura, arg.dispositivo)

if __name__ == '__main__':
    main()


    