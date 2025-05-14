total_miles = 0
total_gallons = 0
overall_average_miles_per_gallon = 0
miles_driven = 0
gallon_used = 0

while miles_driven != -1:
	miles_driven = float(input(" Enter Miles Driven and stop -1 : " ));
	if miles_driven == -1:
		break

	gallon_used = float(input("Enter Gallons used for the trip and enter -1 to stop: "))
	if gallon_used == -1:
		break

	miles_per_gallon = float(miles_driven / gallon_used)	
	
	total_miles += miles_driven
	total_gallons += gallon_used

	overall_average_miles_per_gallon = float (total_miles / total_gallons)


	print(f" Miles per gallon for this trip: {miles_per_gallon} ")

	print(f" the overall average {overall_average_miles_per_gallon}")


