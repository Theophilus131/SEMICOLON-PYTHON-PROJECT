#Write a function sum_list(numbers) that takes a list of numbers and returns the sum using a loop.


number = [2,3,4,5,6,7,8,9]

def sum_list(numbers):
	total = 0
	for number in numbers:
		total += number
	
	return total
result = sum_list(number)
print(f" sum of numbers in the list {result} ")


