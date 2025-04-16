#!/usr/bin/python3

from src.classes.uProcessorsStates import uProcessorsStates as uPStateMachine
from src.functions.upParser import createParser

def main() -> None:

    args = createParser()
    sm = uPStateMachine()

    var = 10
    match var:
        case 1:
            print(1)
        case 2:
            print(2)
        case _:
            print('general')



if __name__ == '__main__':
    main()
