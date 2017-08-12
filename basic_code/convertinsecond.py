hours = float(input("Enter number of hour: "))
minutes = float(input("Enter number of minutes: "))
seconds= float(input("Enter number of seconds: "))

def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds
print(to_secs(hours, minutes, seconds))