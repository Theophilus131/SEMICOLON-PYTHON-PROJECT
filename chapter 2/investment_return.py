principal = int (1000)
annual_rate = float (7 / 100)
number_year  = 10

amount_deposit =float( principal * (1 + annual_rate) ** number_year)

print("The amount in return in 10 years is",  amount_deposit)