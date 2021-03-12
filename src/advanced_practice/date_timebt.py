from  datetime import date
from  datetime import time
from  datetime import datetime

objDate=date(year=2020,month=1,day=28)
print("Date",objDate)

objDate=time(hour=13,minute=1,second=31)
print("Time",objDate)

objDateTime=datetime(year=2020,month=1,day=28,hour=13,minute=14,second=31)
print("Datetime",objDateTime,objDateTime)

stamp=datetime.timestamp(objDateTime)
print("Date and Time ",objDateTime,"->Timestamp",stamp)
dateTimeFromTimestamp=datetime.fromtimestamp(stamp)
print("Timestamp:",stamp,"->Date and Time ",dateTimeFromTimestamp)


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


mydaynow=datetime(year=2020,month=1,day=31,hour=17,minute=3,second=5)
print("Ngay doi la ",mydaynow.strftime("%A %I:%M:%S%p"))

a=3.34567
print("so la {:.2f}".format(a))

print("Lam tron {:.0f}".format(a))

b=1
print("them 0: {:A>3d}".format(b))

c=10000000
print("tra ve phan ngan {:,}".format(c))

def enumerates(chuoi,start=0):
    n=start
    for elem in chuoi:
        yield n,elem
        n+=1

a=['mot','hai','ba','bon']
b=print(list(enumerates(a,start=0)))

for index, item in enumerates(a):
    print(item, index)


for index, item in enumerate(a):
    print(item, index)

print(enumerates(a,start=0))

n = int(input("Nhap vao so nguyen thu nhat"))
m = int(input("Nhap vao so nguyen thu hai"))
for i in range (n, m + 1):
    print(i)



