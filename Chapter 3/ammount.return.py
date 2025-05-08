principal = int (1000)
annual_rate = float (7 / 100)

for number in range (1, 31):
	number_year = int(input("Enter the number of years")
	amount_deposit =float( principal * (1 + annual_rate) ** number_year)


print("The amount in return ",  amount_deposit)