from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json
import webbrowser


def getMapImage(lat, lng):
    urlbase = "http://maps.google.com/maps/api/staticmap?"
    GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
    args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,12,400,400,"hybrid",lat,lng)
    args = args + "&key=" + GOOGLEAPIKEY
    mapURL = urlbase+args
    urlretrieve(mapURL, 'googlemap.png')


getMapImage(38.266,-110.719)


