 #Task: Write a function count_even(numbers) that counts how many even numbers are in a given list.

number = [2,3,4,5,6,7,8,9]

def count_even(numbers):
	count = 0
	for number in numbers:

		if number % 2 == 0:
			
			count += 1

	return count


result = count_even(number)
print(f" the even number is {result}")


		