print("EEROR CATCHING USING TRY AND EXCEPTION")

"""
try:
	number = int(input("enter a number :"))
	print(number)
except:
	print("invalid input") 
"""

try:
	# value = 10/0
	number = int(input("enter a number :"))
	print(number)
except ZeroDivisionError:
	print("Divided by Zero ")
except ValueError:
	print("invalid input") 
