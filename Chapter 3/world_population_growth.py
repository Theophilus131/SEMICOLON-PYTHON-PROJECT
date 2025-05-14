growth_rate = float(0.85/100)

current_world_population = 8_231_613_070

print("...........world population growth table..............") 

for year in range(1, 101):
	current_world_population *=  (1+ growth_rate)
	

	print(f" Year {year}:   {current_world_population}")


