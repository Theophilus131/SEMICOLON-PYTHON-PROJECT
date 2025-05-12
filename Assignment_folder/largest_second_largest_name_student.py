	
number_of_student = int(input ("Enter number of students: "))

second_highest = 0
highest = 0
name = " "
second_name = " "
students_name = " "
student_score = 0
	
for number in range(1, number_of_student +1):
	student_score= int(input("Enter students score : "))
	students_name= input("Enter students names: ")

if(student_score == highest):
	second_highest = highest
	highest = student_score
	
if student_score > highest:
	second_highest = highest
	highest = student_score

if student_score == highest:
	second_name = students_name
	name = students_name
	
if student_score > highest:
	second_Name = students_name
	name = students_name

print(f"The name of students is:  {name}")
print(f"The student with the highest score is: {highest}")


print(f"the name of student with the second highest is: {second_name}")
print(f"The student with the second highest score is: {second_highest}")