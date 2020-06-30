import argparse
from utils import *

def main():
	# create argument parser object 
	parser = argparse.ArgumentParser(description = "Welcome To Geo Sight \033[93m geosight -lat LATITUTE -lon LONGITUTE \033[00m  ") 
  
	parser.add_argument("-lat", "--latitute", type = str, nargs = 1, 
	                    metavar = "lat", help = "Latitute") 

	parser.add_argument("-lon", "--longitute", type = str, nargs = 1, 
	                    metavar = "lon",  help = "Longitute") 

	# parse the arguments from standard input 
	args = parser.parse_args()

	get_details(args.latitute[0],args.longitute[0])
	print(args.latitute[0],args.longitute[0],sep=" ")	


if __name__ == "__main__":
	main()
