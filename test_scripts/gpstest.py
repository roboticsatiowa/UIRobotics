import math

#c for current, t for target
cHeading = 0 #degrees from east. TODO: use sensor to constantly update this
tHeading = 0
cLat = 100 #from GPS sensor
cLong = 20
tLat = 50
tLong = 10

#for future reference, calculations will be long over lat

tHeading = math.atan((tLong-cLong)/(tLat-cLat))

tHeading = math.degrees(tHeading)

if cLat > tLat:
    tHeading += 180


print(tHeading)
