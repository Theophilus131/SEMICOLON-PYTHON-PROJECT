
from random import randint

numbers = []

def random_number():
	for number in range(10):
		number = randint(1, 51)
		numbers.append(number)
	return numbers

def length_list(numbers):
	count = 0
	for number in numbers:
		count += 1
	return count

def sum_element_even_position(numbers):
	sum_even_position = 0
	count = 0

	for number in numbers:
		if count % 2 == 0:
			sum_even_position += number
		count += 1
	return sum_even_position


def sum_element_odd_position(numbers):
	sum_odd_position = 0
	count = 0
	for number in numbers:
		if count % 2 != 0:
			sum_odd_position += number
		count += 1
	return sum_odd_position

def multiply_element_third_position(numbers):
	multiply = 1
	index = 0
	for number in numbers:
		if (index + 1) % 3 == 0:
			multiply *= number

		index += 1

	return multiply

def average_element(numbers):
	total = 0
	average = 0
	count = length_list(numbers)

	for number in numbers:
		total += number

	average = total / count

	return average





