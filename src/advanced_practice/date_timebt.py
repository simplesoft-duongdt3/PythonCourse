from  datetime import date
from  datetime import time
from  datetime import datetime


objDate=date(year=2020,month=1,day=28)
print("Date",objDate)

objDate=time(hour=13,minute=1,second=31)
print("Time",objDate)

objDateTime=datetime(year=2020,month=1,day=28,hour=13,minute=14,second=31)
print("Datetime",objDateTime,objDateTime)

timestamp=datetime.timestamp(objDateTime)
print("Date and Time ",objDateTime,"->Timestamp",timestamp)
dateTimeFromTimestamp=datetime.fromtimestamp(timestamp)
print("Timestamp:",timestamp,"->Date and Time ",dateTimeFromTimestamp)


date1=datetime(year=2020,month=1,day=31,hour=1,minute=3,second=5)
date2=datetime(year=2030,month=3,day=31,hour=12,minute=13,second=5)

delta=date2-date1

a= 10 - 19
print("TimeDelta difference :",date2,"-",date1,"=",delta,type(delta))


myString="2020-10-16"

myDate=datetime.strptime(myString,"%Y-%m-%d")
print("Convert text ",myString,"to dateTime ",myDate)

myFormatText=myDate.strftime("%Y/%m/%d")
print("Convert Datetime",myDate,"to next",myFormatText)

myday= date(year=2020,month=12,day=27)
print("ngay da doi ",myday.strftime("%A %Y/%m/%d"), myday.weekday())