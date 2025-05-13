e_estimate = 1
factorial = 1

for e in range(1, 11):

	factorial *= e
	e_estimate += 1 / factorial

print(f" estimated value of e after 10 terms {e_estimate} ")