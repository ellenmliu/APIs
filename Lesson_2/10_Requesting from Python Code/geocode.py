import httplib2
import json

def getGeocodeLocation(place):
  google_api_key = "AIzaSyBei52rTRzG5k-oeWA-ZuOZgNU2O0C8Rtk"
  locationString = place.replace(" ","+")
  url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %
         (locationString, google_api_key))
  h = httplib2.Http()
  result = json.loads(h.request(url,'GET')[1])
  latitude = result['results'][0]['geometry']['location']['lat']
  longitude = result['results'][0]['geometry']['location']['lng']
  return (latitude,longitude)
