import datetime
dt = datetime.datetime.now()
print(dt)

dt1 = datetime.datetime(2017,12,10,11,23,43,11)
print(dt1)

dt1 = datetime.datetime(2017,12,10)
print(dt1)

delta = datetime.timedelta(days=11,hours=10,minutes=15,seconds=38,milliseconds=13,microseconds=13)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())
print(delta)

dt2 = datetime.datetime.now()
print(dt2)
tdate = datetime.timedelta(days=1000)
print(dt2 + tdate)
print(dt2 - tdate)

oct22st = datetime.datetime(2017,10,22,16,10,23)
today = datetime.datetime.now()
print("Full dayname",oct22st.strftime("%A"))
print("Full dayname",today.strftime("%A"))
print("small dayname",oct22st.strftime("%a"))
print("small dayname",today.strftime("%a"))
print(oct22st.strftime("%m/%Y/%d"))
print(oct22st.strftime("%I:%M %p"))
print(datetime.datetime.strptime("March,21,2017",'%B,%d,%Y'))
