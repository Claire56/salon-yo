from flask import Flask ,render_template, session,jsonify, request ,redirect, make_response
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sqlalchemy import func
import pandas as pd
import json
import os
import secrets
from geocode import longLat


app = Flask('__name__')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ.get('secret_key')

# other keys used by the app
google_api_key = os.environ.get('google_api_key')
four_square_client = os.environ.get('foursquare_client_id')
four_square_key= os.environ.get('foursquare_client_secret')


@app.route('/')
def home():

	return render_template('home.html')


@app.route('/salon')
def salonType():
	need = request.get('need')
	loc = request.get('loc')
	# get latitude and longtude
	lat, lng = longLat(loc)
	cid =os.environ['foursquare_client_id']
	cs =os.environ['foursquare_client_secret']

	#Four square api to get the salon with the requested need
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s,&radius=%s' % (cid, cs,lat,lng,need,100))
	h= httplib2.Http()
	r= json.loads(h.request(url, 'GET')[1])


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
        # print("Salon Name: %s" % salonInfo['name'])
        # print("Salon Address: %s" % salonInfo['address'])
        # print("Image: %s \n" % salonInfo['image'])
		return render_template('salon.html',salonInfo=salonInfo) 
	else:
        # print("No places Found for %s" % location)
        # return "None Found"
	    return render_template('not_found.html')






if __name__=='__main__':


	DebugToolbarExtension(app)
	app.run(debug = True , host = "0.0.0.0")
