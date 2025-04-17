#!/usr/bin/python3

from src.functions.PlotParser import create_parser as cli_args

def main() -> None:
    args = cli_args()
    if args.local_config:
        print('Theres local config')
    if args.input_file:
        print('Theres input file')


if __name__ == '__main__':

    main()
