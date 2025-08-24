#!/usr/bin/python3

from src.classes.calendarHandler import calendarHandler
from src.functions.calendarUtils import calendarSetUp
import datetime
import pytz

def main() -> None:
    
    orquestrator = calendarHandler()
    orquestrator.calendarObj = calendarSetUp()
    orquestrator.getCalendars()
   

    '''
    START TESTING FUNCTIONALITY OF THE CALENDAR

    for calendar in orquestrator.calendars:
        calendar_id = calendar['id']
        print(f"\n--- Events in calendar: {calendar.get('summary', calendar_id)} ---")
        events_result = orquestrator.calendarObj.events().list(
            calendarId=calendar_id,
            timeMin=orquestrator.startTime,
            timeMax=orquestrator.endTime,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        if not events:
            print("No events today")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event.get('summary', 'No title'))

    END TESTING FUNCTIONALITY OF THE CALENDAR
    '''

if __name__ == '__main__':
    main()
