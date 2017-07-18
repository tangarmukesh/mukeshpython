time = float(input("Input time in seconds: "))
month = time // (30*7*24*3600)
time = time % (30*7*24*3600)
week = time //  (7*24*3600)
time = time % (7*24*3600)
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("m:w:d:h:m:s->%d:%d:%d:%d:%d:%d" % (month,week,day,hour, minutes, seconds))