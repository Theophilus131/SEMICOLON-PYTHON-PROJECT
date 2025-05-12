number_of_students = int(input("Enter number of students: ")) 

highest = 0
name = ""

for _ in range(number_of_students):
	student_name = input("Enter student's name: ")
	student_score = int(input("Enter student's score: "))

if student_score > highest:
	highest = student_score
	name = student_name

print(f"The student with the highest score is: {name}")
print(f"The highest score is: {highest}")
