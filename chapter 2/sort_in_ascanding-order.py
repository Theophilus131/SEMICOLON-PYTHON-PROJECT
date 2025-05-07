first_number = float(input("enter first number : "))

second_number = float(input("enter second number : "))

third_number = float(input("enter third number : "))


if first_number <= second_number and first_number <= third_number:
    if second_number <= third_number:
        print(first_number, second_number, third_number)
    else:
        print(first_number, third_number, second_number)

if second_number <= first_number and second_number <= third_number:
    if first_number <= third_number:
        print(second_number, first_number, third_number)
    else:
        print(second_number, third_number, first_number)

if third_number <= first_number and third_number <= second_number:
    if first_number <= second_number:
        print(third_number, first_number, second_number)
    else:
        print(third_number, second_number, first_number)
