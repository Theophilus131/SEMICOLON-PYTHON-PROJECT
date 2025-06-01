#Write a function find_max(numbers) that returns the largest number in a list without using max().

number = [2,3,4,5,6,7,8,9]

def find_max(numbers):
	largest = numbers[0]

	for number in numbers:
		if number > largest:
			largest = number
	return largest

result = find_max(number)
print(f" the largest number is {result}")