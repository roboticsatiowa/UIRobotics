from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json
import webbrowser

def ifValidLatitude(x):
    try:
        x = float(x)
    except:
        if not isinstance(x, float):
            print("Invalid input")
            return False
    if x > 90 or x < -90:
        print("Invalid input")
        return False
    return True

def ifValidLongitude(x):
    try:
        x = float(x)
    except:
        if not isinstance(x, float):
            print("Invalid input")
            return False
    if x > 180 or x < -180:
        print("Invalid input")
        return False
    return True
# 10/07/2021 Charlie - taking input GPS coordinates and only accepting floats

lat = input("Enter latitude: ")
while not ifValidLatitude(lat):
    lat = input("Enter latitude: ")

lng = input("Enter longitude: ")
while not ifValidLongitude(lng):
    lng = input("Enter longitude: ")
# 10/10/2021 Charlie - finished taking in GPS coordinates with valid inputs

def getMapImage(lat, lng):
    urlbase = "http://maps.google.com/maps/api/staticmap?"
    GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
    args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,12,400,400,"hybrid",lat,lng)
    args = args + "&key=" + GOOGLEAPIKEY
    mapURL = urlbase+args
    urlretrieve(mapURL, 'googlemap.png')

getMapImage(lat, lng)
# getMapImage(38.266,-110.719)
