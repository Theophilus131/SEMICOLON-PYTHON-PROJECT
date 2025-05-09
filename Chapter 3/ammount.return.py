principal = int (1000)
annual_rate = float (7 / 100)

for number_year in range (1, 31):
	print(f" {float( principal * (1 + annual_rate) ** number_year) :.2f}")