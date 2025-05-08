total_miles = 0
total_gallons = 0
overall_average_miles_per_gallon

while miles_driven != -1:
	miles_driven = float(input(" Enter Miles Driven and stop -1 " ));
	if miles_driven == -1:
	break

gallon_used = float(input("Enter Gallons used for the trip and enter -1 to stop"))

miles_per_gallon = float(miles_driven // gallon_used)	
	
total_miles += miles_driven
total_gallons += gallons_used

overall_average_miles_per_gallon = total_miles / total_gallons


print(f" Miles per gallon for this trip: %.2f%n {overallMPG} ")

print(f" the overall average {overall_average_miles_per_gallon}")


