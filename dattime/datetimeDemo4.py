#add..
import datetime

today = datetime.datetime.today()
print(today)

#add 10 days
fd = today+datetime.timedelta(days=10)
print(fd)

#years
fd2 = fd + datetime.timedelta(days=365*2,hours=5)
print(fd2)
#sub
#min
#sec

#compare date

d1 = datetime.datetime.today()
d2 = d1 + datetime.timedelta(days=1)

print(d1<d2)
print(d1>d2)
print(d1 == d2)