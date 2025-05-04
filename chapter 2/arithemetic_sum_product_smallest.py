first_number =  int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number"))

largest = first_number;
smallest = first_number;


sum = first_number + second_number + third_number

average = float( sum / 3)

product =  first_number * second_number * third_number


print("numbers added resulted in: ", sum)

print("average of number is", average)

print("product od numbers ", product)

if second_number > largest:
	print("largest is ", second_number)

if third_number > largest:
	print("largest is ", third_number)

if second_number < smallest:
	print("smallest is ", second_number)

if third_number < smallest:
	print("smallest is ", third_number)


