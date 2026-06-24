#string fmt
import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%d/%m/%y"))
print(now.strftime("%d/%m/%Y : %I %H %M %S"))
print(now.strftime("%d/%m/%y %A %a"))
print(now.strftime("%d/%m/%y %B"))
print(now.strftime("%d/%m/%y %b"))
print(now.strftime("%d/%m/%y %p"))

date_str  ="24-06-2026"

d = datetime.datetime.strptime(date_str,"%d-%m-%Y")
print(d)