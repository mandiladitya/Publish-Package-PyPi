from datetime import date
from geopy import Nominatim
import datetime
import wolframalpha
def get_details(lat,lon):
	coord=[]
	coord.append(lat)
	coord.append(lon)
	geolocator=Nominatim(user_agent="test/1")
	#print('{coord[0]},{coord[1]}')
	coord1="{},{}".format(lat,lon)
	location =geolocator.reverse(coord1)
	s=location.address

	final=s.split(",")
	#print(final)
	locatity=final[0]
	city=final[2]
	pincode=final[-2]
	state=final[-3]
	country=final[-1]
	query1="temperature of {}".format(city)
	query2="Humidity of {}".format(city)
	client = wolframalpha.Client('AGVT22-AE67Q6APHU')
	print("\033[93m MONITORING ...\033[00m")
	try:
		res = client.query(query1)
		res2=client.query(query2)
		results = next(res.results).text
		results2 = next(res2.results).text
		print("=============\033[92m WELCOME TO GEOSIGHT \033[00m=================")
		print('\033[96m Latitute : {}\033[00m '.format(lat))
		print('\033[96m Longitute : {}\033[00m '.format(lon))
		print('\033[96m Locality : {}\033[00m '.format(locatity))
		print('\033[96m City : {}\033[00m '.format(city))
		print('\033[96m State : {}\033[00m '.format(state))
		print('\033[96m Country : {}\033[00m '.format(country))
		print('\033[96m Temperature : {}\033[00m '.format(results))
		print('\033[96m Humidity : {}\033[00m '.format(results2))
		print("======================================")
	except:
		print("=============\033[92m WELCOME TO GEOSIGHT \033[00m=================")
		print('\033[96m Latitute : {}\033[00m '.format(lat))
		print('\033[96m Longitute : {}\033[00m '.format(lon))
		print('\033[96m Locality : {}\033[00m '.format(locatity))
		print('\033[96m City : {}\033[00m '.format(city))
		print('\033[96m State : {}\033[00m '.format(state))
		print('\033[96m Country : {}\033[00m '.format(country))
		print('\033[91m Temperature : Sorry ! Not Reognized\033[00m')
		print('\033[91m Humidity: Sorry ! Not Reognized\033[00m')
		print("======================================")
