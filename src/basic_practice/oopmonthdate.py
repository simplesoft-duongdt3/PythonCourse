
from datetime import date

from datetime import time
from datetime import datetime


objDate=date(year=2020,month=1,day=31)
print("Date",objDate)

objTime=time(hour=13,minute=14,second=31)
print("Time",objTime)

objDateTime= datetime(year=2020,month=1,day=31,hour=14,second=31)
print("DateTime",objDateTime)

timestamp=datetime.timestamp(objDateTime)
print("DAte and Time",objDateTime,"Timestamp",timestamp)
dateTimeFromTimeStamp=datetime.fromtimestamp(timestamp)
print("Timestamp",timestamp,"Date and Time",dateTimeFromTimeStamp)

date1=datetime(year =2018,month=1,day=31,hour=1,minute=3,second=5)
date2=datetime(year =2020,month=3,day=12,hour=13,minute=13,second=25)
delta=date2-date1
print("TimeDelta difference: ", date2, "-" ,delta,type(delta))
print("TimeDelta difference: ", date2, "-" ,delta.total_seconds(),type(delta))

myString="2020-12-28"
myDate=datetime.strptime(myString,"%Y-%m-%d")
print("convert text ",myString,"to Datetime",myDate)
myFormatText=myDate.strftime("%Y/%m/%d")
print(" convert DateTime ", myDate, " To Text",myFormatText)

ngay =date(year=2020,month=12,day=28)
myFormatText1=ngay.strftime("%a %Y/%m/%d")
print(" convert DateTime ", ngay, " To Text",myFormatText1)