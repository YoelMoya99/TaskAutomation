#!/usr/bin/python3

from datetime import datetime
from src.classes.Bugs import Bugs as bugs

def main() -> None: 
    
    title = input("What is the title of the issue? ")
    context = input("What is the context of the issue? ")
    msg = input("What is the description of the issue? ")

    obj_bug = bugs()
    obj_bug.save_bug(
            title,
            context,
            msg,
            datetime.now().strftime("%Y/%m/%d")
            )

if __name__ == '__main__':
    main()
