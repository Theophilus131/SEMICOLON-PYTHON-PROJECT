factorial = 1
number = int(input("Enter number: "))

for number in range(number, 0, -1):
	factorial *= number

print(f" the factorial of number is {factorial}")

