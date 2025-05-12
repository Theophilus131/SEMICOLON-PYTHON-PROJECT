principal = int (1000)
annual_rate = float (7 / 100)


for i in range(0, 30):
	amount_deposit =float( principal  * (1 + annual_rate) ** i)

	print(f" The amount in {i + 1} is {amount_deposit + 1:.2f} ")