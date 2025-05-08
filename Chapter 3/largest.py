

largest = 0
second_largest = 0


for number in range (1, 11):
	first_number = int(input("Enter number: "))
	
	if first_number > largest:
		second_largest = largest
		largest = first_number

	elif first_number > second_largest and first_number != largest:
		second_largest = first_number 



print("the largest of the group is:", largest )
print("the second largest is: ", second_largest)