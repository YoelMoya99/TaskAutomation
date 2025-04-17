#!/usr/bin/python3

from src.functions.PlotParser import create_parser as cli_args

def main() -> None:
    args = cli_args()
    print('\nTesting command line arguments\n')
    print('This arguments where inputted')
    print(args)

if __name__ == '__main__':

    main()
