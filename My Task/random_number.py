import random

score = 0

for number in range(1, 11):

	first_number = random.randrange(1, 11)
	second_number = random.randrange(1, 11)

	if first_number < second_number:
	
		temp = first_number
		first_number = second_number
		second_number = temp
	
	answer = first_number - second_number

	print(f" Question {number} what is {first_number} - {second_number}?")
	user_input = int(input("your answer: "))

	if user_input == answer:
		print("you answered correctly! \n")
		score += 1
	else:
		print(f" wrong answer. the correct answer is {answer}\n")

print(f" you got {score} out of 10 question correct." )