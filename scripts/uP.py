#!/usr/bin/python3

from src.classes.uProcessorsStates import uProcessorsStates as uPStateMachine
from src.functions.upParser import createParser

def main() -> None:

    args = createParser()
    sm   = uPStateMachine()

    sm.presentState = sm.State1

    if args.genPDF:
        sm.typeProcess  = 'pdf'
    elif args.genMD:
        sm.typeProcess  = 'md'

    sm.rubric       = args.rubric
    sm.inDir        = args.inDir
    sm.outDir       = args.outDir

    while not sm.endProcess:
        sm.presentState()

if __name__ == '__main__':
    main()
