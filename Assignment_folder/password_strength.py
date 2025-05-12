password = input("Enter your password: ")

password_length = len(password)

if password_length < 8:
	print("Password entered is VERY WEAK")

if password_length == 8:
	print("Password entered is WEAK")

if password_length > 8 and password_length < 16:
	print("Password entered is STRONG")

if password_length > 16:
	print("Password entered is VERY STRONG")