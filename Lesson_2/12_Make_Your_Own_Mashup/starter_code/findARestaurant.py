from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "FAXWGJU1T5JKZMQBVUFBBZ0CK1ZXP130JWQ0TMQW33LTIV0C"
foursquare_client_secret = "52TF4CEXKTNKN1HSRREGPWPDVSRA0030ST2H5RG3XQ2IGLWD"
foursquare_version = "20170101"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	lat, long = getGeocodeLocation(location)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=%s&ll=%s,%s&query=%s' %
               (foursquare_client_id, foursquare_client_secret, foursquare_version, str(lat), str(long), mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	
	#3. Grab the first restaurant
	if result['response']['venues']:
          restaurant = result['response']['venues'][0]
          name = restaurant['name']
          venue_id = restaurant['id']
          address = restaurant['location']['formattedAddress']
          formatted_address = ""
          for i in address:
            formatted_address += i + " "
            
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
          url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=%s' %
                 (venue_id, foursquare_client_id, foursquare_client_secret, foursquare_version))
          h = httplib2.Http()
          result = json.loads(h.request(url,'GET')[1])
          
	#5. Grab the first image
          if result['response']['photos']['items']:
            firstpicture = result['response']['photos']['items'][0]
            pre = firstpicture['prefix']
            suf = firstpicture['suffix']
            imgurl = pre + "300x300" + suf
	#6. If no image is available, insert default a image url
          else:
            imgurl = "https://cdn.pixabay.com/photo/2016/02/05/15/34/pasta-1181189_1280.jpg?direct"
	#7. Return a dictionary containing the restaurant name, address, and image url
          restaurant_info = {'name':name, 'address':formatted_address, 'img':imgurl}
          print "Restaurant name: " + name + "\nRestaurant Adress: " + formatted_address + "\nImage: " + imgurl + "\n"
          return restaurant_info
        else:
          print "No restaurants found in %s" % location
          return "No restaurants found in %s" % location
      
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
