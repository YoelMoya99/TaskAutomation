import pytz
import datetime
import pandas as pd

class calendarHandler:

    def __init__(self):
        self.tz = pytz.timezone('America/Costa_Rica')
        self.now = datetime.datetime.now(self.tz)
        self.startTime = datetime.datetime(self.now.year, self.now.month, self.now.day, 0, 0, 0, tzinfo=self.tz).isoformat()
        self.endTime = datetime.datetime(self.now.year, self.now.month, self.now.day, 23, 59, 59, tzinfo=self.tz).isoformat()
        self.calendarObj = None
        self.calendars = None

    def testPrint(self):
        print("Start of day:", self.startTime)
        print("End of day:", self.startTime)

    def getCalendars(self):
        calendar_list = self.calendarObj.calendarList().list().execute()
        self.calendars = calendar_list.get('items', [])

    def printCalendars(self):

        self.getCalendars()

        for calendar in self.calendars:
            calendar_id = calendar['id']
            print(f"\n--- Events in calendar: {calendar.get('summary', calendar_id)} ---")
            events_result = self.calendarObj.events().list(
                calendarId=calendar_id,
                timeMin=self.startTime,
                timeMax=self.endTime,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            
            events = events_result.get('items', [])
            if not events:
                print("No events in that range")
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event.get('summary', 'No title'))


    def pushEvent(self, path):
   
        df = pd.read_excel(path)

        for index, row in df.iterrows():
            calendar_id = row['calendarID']
            title = row['summary']
            description = row['description']
            startTime = pd.to_datetime(row['startTime']).isoformat() 
            endTime = pd.to_datetime(row['endTime']).isoformat()
            timezone = row['timeZone']


            event_body = {
                'summary': title,
                'description': description,
                'start': {
                    'dateTime': startTime,
                    'timeZone': timezone
                },
                'end': {
                    'dateTime': endTime,
                    'timeZone': timezone
                }
            }
    
            event = self.calendarObj.events().insert(
                calendarId=calendar_id,
                body=event_body
            ).execute()
    
            print(f"Event created: {event.get('htmlLink')}")





