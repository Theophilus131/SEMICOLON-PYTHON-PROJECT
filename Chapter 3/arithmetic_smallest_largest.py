
total = 0
average = 0
product = 1
smallest = 0
largest = 0

for number in range(1, 5):
	number = int(input(f" enter the number: "))

	total += number
	average = float(total / 4)
	product = number * product

	if number == 1:
		first_input = number
		smallest = number
		largest = number

	else:
		if number < smallest:
			smallest = number
		if number > largest:
			largest = number


print(f" the sum of the number is {total}") 
print(f" the product of the number is {product}") 
print(f" the average is {average}") 
print(f" the smallest is {smallest}")
print(f" the largest is {largest}")