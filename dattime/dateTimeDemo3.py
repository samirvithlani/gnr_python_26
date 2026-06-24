#mills..
#date ->1st jan 1970

import datetime

now = datetime.datetime.now()
print(now.timestamp())


x =datetime.datetime.fromtimestamp(0)
print(x)

x1 = datetime.datetime.fromtimestamp(now.timestamp())
print(x1)
