time = float(input("Input time in seconds: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("h:m:s->%d:%d:%d" % (hour, minutes, seconds))