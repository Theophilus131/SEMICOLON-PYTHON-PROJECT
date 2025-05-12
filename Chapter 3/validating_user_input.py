number_input = int(input("Enter user number: "))

passes = 0
counter = 1

while counter <= number_input:
    result = input("Enter result (1 = pass, 2 = fail): ")
    
    while result not in ('1', '2'):
        result = input("Invalid input. Enter 1 (pass) or 2 (fail): ")

if result == '1':
	passes += 1
	counter += 1

failures = number_input - passes

print(f"Passed: {passes}")
print(f"Failed: {failures}")


