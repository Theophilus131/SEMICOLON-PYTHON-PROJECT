number = int(input("Enter 5 digit number:  "))

for i in the range(1, number, 1):
if number < 10000 or number > 99999:
	print("invalid number enter 5 digit number")
else:
	first_number = int(number // 10000) % 10
	second_number = int(number // 1000) % 10
	third_number = int(number // 100)   % 10
	fourth_number = int (number // 10)   % 10
	fifth_number = int (number % 10)


print( first_number, second_number, third_number,fourth_number,fifth_number, "\t")