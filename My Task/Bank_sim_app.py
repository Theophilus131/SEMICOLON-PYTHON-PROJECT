List = [] 


def main_menu():
	while True:
		message = """
                 Bank app simulation:
                 What Do you want to perform:
                1. Check Account Balance
		2.  Withdraw Money
		3.  Account Details
		4.  Multiple Withdrawal
		00. Exit 
		"""
		print(message)
		user = input("What tractaction do you want to carry out: ")

		match user:
			case "1": Account_Balance_menu()

			case "2": Withdraw_money_menu()

			case "3": Account_details_menu()

			case "4": multiple_withdrawal_menu()

			case "00": 
				print("Exiting bank app ")
				break
			case _: print("Invalid input. Try again.")
			
def Account_Balance_menu():
	while True:
		message = """

		1. balance: 500000
		
		0. Back
		
		"""
		print(message)
		user = input("Enter the balance: ")

		match user:
			case "1": 
				add = input("add what you want to add: ")
				if balance < 0:
					print("invalid balance, balance cannot be negative:")
				List.append(add)
				print(" task added")

			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")


def Withdraw_money_menu():
	while True:
		message = """
		1. Enter withdrawal amount multiples of N500 or N 1000:

		0. Back
		
		"""
		print(message)
		user = input("Enter a number to select: ")

		match user:
			case "1":
				print("here are your tasks: ")
				for index, task in enumerate(Tasks):
					print(f"{index}.{task}")
			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")





def Account_details_menu():
	while True:
		message = """
		1. Account details 
		
		0. Back
		
		"""
		print(message)
		user = input("Enter a number to select: ")

		match user:
			case "1":
				delete = input("enter index of task to delete: ")
				if delete.isdigit():
					delete = int(delete)
				if 0 <= delete < len(Tasks):
					Tasks.pop(delete)
					print("Deleted the task  ")
			
			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")



		
main_menu()




