from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Date, Time, DateTime
    objDate = date(year=2020, month=1, day=31)
    print("Date", objDate)

    objTime = time(hour=13, minute=14, second=31)
    print("Time", objTime)

    objDateTime = datetime(year=2020, month=1, day=31,
                           hour=13, minute=14, second=31)
    print("DateTime", objDateTime, objDateTime)

    # convert current date into timestamp
    timestamp = datetime.timestamp(objDateTime)
    print("Date and Time", objDateTime, "-> Timestamp:", timestamp)
    dateTimeFromTimestamp = datetime.fromtimestamp(timestamp)
    print("Timestamp:", timestamp, "-> Date and Time", dateTimeFromTimestamp)

    # Create two dates
    date1 = datetime(year=2020, month=1, day=31, hour=1, minute=3, second=5)
    date2 = datetime(year=2020, month=3, day=12, hour=13, minute=14, second=31)

    # TimeDelta, difference between two dates, times, datetimes
    delta = date2 - date1
    print("TimeDelta difference: ", date2, "-", date1, "=", delta, type(delta))

    # Today, now
    today = date.today()
    print("Today is: " + str(today))
    print("Today time is: " + str(datetime.now()))

    myString = '2020-10-31'

    # Create date object in given time format yyyy-mm-dd
    myDate = datetime.strptime(myString, "%Y-%m-%d")

    print("Convert text ", myString, "to DateTime", myDate)

    myFormatText = myDate.strftime("%Y/%m/%d")
    print("Convert DateTime ", myDate, "to Text", myFormatText)

if __name__ == "__main__": 
    main()
else: 
    print ("date_time.py imported") 




