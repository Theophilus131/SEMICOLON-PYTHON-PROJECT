growth_rate = float(0.85/100)

current_world_population = 8_231_613_070


for world_population_growth in range(1, 101):
	world_population_growth = current_world_population *growth_rate 
	print(f" {world_population_growth + 1}")