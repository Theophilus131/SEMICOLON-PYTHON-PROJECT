import random

subtraction = 0

def function(first_number, second_number):

	first_number = random.randrange(1, 11)

	second_number = random.randrange(1, 11)
	
	if first_number > second_number:
		subtraction = first_number - second_number

	else: subtraction = first_number - second_number

	return subtraction


for attempt in range(1, 11):

	print(f" subtract {first_number} - {second_number} ")

	user_input = int(input("subtract the two numbers: "))

if  subtraction == user_input:
	print("You ans is correct")
else:
	print("you ans is wrong, try again")
