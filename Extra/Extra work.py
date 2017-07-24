from datetime import date, timedelta
print(date.today())
ydate = date.today() - timedelta(1)
tdate = date.today() - timedelta(-1)
print("Yesterday date: ",ydate)
print("Tomorrow date: ",tdate)