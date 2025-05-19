def categorize_numbers(numbers, divisible_by):

	result = []
	for number in numbers:
		if number % divisible_by == 0:
			result.append(number)
	return result

print(categorize_numbers( [10, 15, 21, 30], 5))



