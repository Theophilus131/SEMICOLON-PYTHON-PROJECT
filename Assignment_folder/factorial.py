factorial = 1
number = int(input("Enter number: "))

while number > 0:
    factorial *= number
    number -= 1

print(f" The factorial is {factorial}")
