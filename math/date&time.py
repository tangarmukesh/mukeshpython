# Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta
print(date.today())
ydate = date.today() - timedelta(1)
tdate = date.today() - timedelta(-1)
print("Yesterday date: ",ydate)
print("Tomorrow date: ",tdate)

# Write a Python program to convert the date to datetime (midnight of the date) in Python.

from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))


# Write a Python program to print next 5 days starting from today.

import datetime
base = datetime.datetime.today()
for x in range(0, 5):
      print(base + datetime.timedelta(days=x))

# Write a Python program to add 5 seconds with the current time.

import datetime
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())

# Write a Python program to drop microseconds from datetime.

import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)






