def get_total(integer):
	if integer >= 1 and integer <= 10000:

		first_number = (integer // 10000) % 10

		second_number = (integer // 1000) % 10

		third_number = (integer // 100)  % 10

		fourth_number = (integer // 10) % 10

		fifth_number = integer % 10


	total = first_number + second_number + third_number + fourth_number + fifth_number

return total

print(get_total(932))
