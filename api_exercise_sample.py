
# Exercise for APIs / Accessing dictionaries and lists:
# APIs do a lot of work for you, but you ultimately you have to be able to parse the data that the API returns to you into a usable format. Let’s parse the Google maps api to grab longitude and latitude data by city name!



from urllib2 import urlopen
from json import load
import geonames


def lat_long(location):
    address=location
    apiUrl = "http://maps.googleapis.com/maps/api/geocode/json?address="+address+"&sensor=false"


    #open the apiUrl and assign data to variable
    response = urlopen(apiUrl)
    json_obj = load(response)
    print json_obj
    
    #hint: #hint open this link in the web browser to help read the JSON object
    #http://maps.googleapis.com/maps/api/geocode/json?address=San%Francisco&sensor=false
        
    
    raw_latlon = json_obj['results'][0]['geometry']['location']
    lat = raw_latlon['lat']
    lon = raw_latlon['lng']
    coord = (lat, lon)
    return coord
    



print lat_long('Mumbai')
print lat_long("Dushanbe")
print lat_long("boston")
print lat_long('san%francisco') #this api link can't have any spaces,replace spaces with '%'

# Take it further:
# Play with finding the latitude and longitude of other places.
# can you loop through a list of cities to output a dictionary with the city’s name  as a key, it’s coordinates as a tuple value? cites = [‘Mumbai’, “Dushanbe”, “Boston”, “Antananarivo”, “London”, “Sydney,Australia”’]

# #sample output
# #{‘Mumbai’: (19.0759837, 72.8776559), ###, ###, ###, ###, ### }

# What else  would you like to build with lat/long data?