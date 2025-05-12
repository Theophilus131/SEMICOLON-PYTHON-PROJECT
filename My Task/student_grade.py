counter_passed = 1
counter_failed = 1

for student in range(10):
	result = int(input("Enter result: "))
	if result == 1:
		counter_passed = counter_passed + 1

	if result == 2:
		counter_failed = counter_failed + 1

print(f" students who passed {counter_passed: }")

print(f" students who failed{counter_failed: }")
