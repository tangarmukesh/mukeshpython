time = float(input("Input time in seconds: "))
week = time //  (7*24*3600)
time = time % (7*24*3600)
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("w:d:h:m:s->%d:%d:%d:%d:%d" % (week,day,hour, minutes, seconds))