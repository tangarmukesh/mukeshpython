units = int(input('Enter the number of units consumed: '))
if units <= 100:
    cost = units * 0.40
    print(cost)
elif units > 100 and units <= 300:
    cost = 100 * 0.40
    extraunits = units - 100
    cost = extraunits * 0.50 + cost
elif units > 300:
    cost = 100 * 0.40
    cost = 200 * 0.50 + cost
    extraunits = units - 300
    cost =  extraunits * 0.60 + cost
metercharge = 50
totalcost = cost + metercharge
print('The total charges are', totalcost)