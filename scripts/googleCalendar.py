#!/usr/bin/python3

from src.classes.calendarHandler import calendarHandler
from src.functions.calendarUtils import calendarSetUp
import datetime
import pytz

def main() -> None:
    
    orquestrator = calendarHandler()
    orquestrator.calendarObj = calendarSetUp()
    orquestrator.printCalendars()   
    orquestrator.pushEvent('events.xlsx')


if __name__ == '__main__':
    main()
