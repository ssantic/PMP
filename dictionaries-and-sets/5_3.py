rainfall_dict = {}

while True:
	city = raw_input("Please enter a city name, or just press RETURN to exit: ")
	if city == '':
		# print cities
		for key in rainfall_dict:
			print key + ": " + rainfall_dict[key]
		break		
	else:
		rainfall = raw_input("Please enter rainfall in millimeters: ")
		rainfall_dict[city] = rainfall