#!/usr/bin/python3

from src.classes.uProcessorsStates import uProcessorsStates as uPStateMachine
from src.functions.upParser import createParser

def main() -> None:

    args = createParser()
    sm = uPStateMachine()

    sm.presentState = sm.State1
    sm.presentState()
    sm.presentState()

if __name__ == '__main__':
    main()
