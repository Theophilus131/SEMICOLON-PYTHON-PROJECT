
total = 0
average = 0
product = 1
smallest = 0

for number in range(1, 5):
	number = int(input(f" enter the number: "))
	total += number
	average = float(total / 4)
	product = number * product

print(f" the sum of the number is {total}") 
print(f" the product of the number is {product}") 
print(f" the average is {average}") 