"""
total_score = 0
for number in range(1, 11):
	score = int(input(f"Enter the student score for student {number}: "))
	total_score += score

average = total_score / number

print(f"The total score is {total_score} and the average is {average}")
"""

total_score = 0
number = 0
score = int(input("Enter the student score for student: "))
while score != -1:
	number += 1
	total_score += score
	score = int(input("Enter the student score for student: "))
	
average = total_score / number

print(f"The total score is {total_score} and the average is {average}")
