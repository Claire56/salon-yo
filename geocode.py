import httplib2
import json
import os
from flask import Flask ,request 



def longLat(city):
    # use google maps to get the longitude and latitude of the city
    location = city.replace(" ", "+")
    google_key = os.environ.get("google_api_key")

    url = (f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_key}')
    h = httplib2.Http()
    # An HTTP client is created with httplib2.HTTP(). A new HTTP request is
    # created with the request() method; by default, it is a GET request. The return value is a tuple
    # of response and content. we take the conten at index zero
    

    r= h.request(url, 'GET')
    results = json.loads(r[1])
    print(results)
    latitude =results['results'][0]['geometry']['location']['lat']
    longitude =results['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)
    # return results


# print(longLat('los angeles CA'))


def salonType(need,loc):
    # need = request.get('need')
    # get latitude and longtude
    lat, lng = longLat(loc)
    cid =os.environ['foursquare_client_id']
    cs =os.environ['foursquare_client_secret']

    #Four square api to get the salon with the requested need
    url = "https://api.foursquare.com/v2/venues/search?"
    payload = {'intent': 'browse', 'v':20150603, 'radius':100 , 'query': need, 'll': (lat,lng), 'client_id': cid , "client_secret":cs}

    h= httplib2.Http()
    r= json.loads(h.request((url,payload),'GET')[1])


    if result['response']['venues']:
        #3.  Grab the first restaurant
        salon = result['response']['venues'][0]
        venue_id = salon['id'] 
        salon_name = salon['name']
        salon_address = salon['location']['formattedAddress']
        address = ""
        for i in salon_address:
            address += i + " "
        salon_address = address
        #4.  Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,cid,cs)))
        result = json.loads(h.request(url, 'GET')[1])
        #5.  Grab the first image
        if result['response']['photos']['items']:
            firstpic = result['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            imageURL = prefix + "300x300" + suffix
        else:
            #6.  if no image available, insert default image url
            imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
        #7.  return a dictionary containing the restaurant name, address, and image url
        salonInfo = {'name':salon_name, 'address':salon_address, 'image':imageURL}
        print("Salon Name: %s" % salonInfo['name'])
        print("Salon Address: %s" % salonInfo['address'])
        print("Image: %s \n" % salonInfo['image'])
        return salonInfo
    else:
        print("No places Found for %s" % location)
        return "None Found"


if __name__ == '__main__':
    salonType("Pizza", "Tokyo, Japan")
    
    
