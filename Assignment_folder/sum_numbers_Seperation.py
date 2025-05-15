integer = int(input("Enter numbers: "))

if integer >= 1 and integer <= 10000:

	first_number = (integer // 10000) % 10

	second_number = (integer // 1000) % 10

	third_number = (integer // 100)  % 10

	fourth_number = (integer // 10) % 10

	fifth_number = integer % 10

	total = first_number + second_number + third_number + fourth_number + fifth_number

	print(f" sum of number is {total}")

else:
	print("enter a valid number")