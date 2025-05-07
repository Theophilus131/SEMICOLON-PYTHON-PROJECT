
number = int(input("Enter 5 digit number:  "))

if number < 10000 or number > 99999:
	print("invalid number enter 5 digit number")
else:
	first_number = int(number // 10000) % 10
	second_number = int(number // 1000) % 10
	third_number = int(number // 100)   % 10
	fourth_number = int (number // 10)   % 10
	fifth_number = int (number % 10)

if first_number == fourth_number & second_number == fifth_number:
	print("number entered is a palindrome: ")
else:

	print("number entered is not a palindrome: ")