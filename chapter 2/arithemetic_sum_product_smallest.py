first_number =  int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

largest = first_number;
smallest = first_number;


total = first_number + second_number + third_number

average = float( total / 3)

product =  first_number * second_number * third_number


print("numbers added resulted in: ", total)

print("average of number is", average)

print("product of numbers ", product)


if second_number > largest:
	largest = second_number
	
if third_number > largest:
	largest = third_number
	
if second_number < smallest:
	smallest = second_number
	
if third_number < smallest:
	smallest = third_number

	
print("Largest number is: ", largest)
print("Smallest number is: ", smallest)


