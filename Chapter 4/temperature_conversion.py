
def fahrenheit(C):
	
	return (9/5) * C + 32
print(f"{'celcius':>10} {'fahrenheit':>15}")
for C in range(0, 101):
	f = fahrenheit(C)
	print(f"{C:>10} {f:>15.1f}")