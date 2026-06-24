import datetime as dt

today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now)

time = dt.datetime.now().time()
print(time)

#custome date..

bd = dt.date(2006,2,14)
print(bd)

bd = dt.datetime(2012,2,14,11,55,00)
print(bd)

#date component...
today = dt.date.today()
print(today.year)
print(today.month)
print(today.day)

#weekday
print("weekday",today.weekday()) #0->Mon,

#timecompon

time = dt.datetime.now()
print("hour",time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)


today =dt.date.today()
mybd=dt.date(2010,2,14)

diff = today-mybd
print("days",diff.days)
