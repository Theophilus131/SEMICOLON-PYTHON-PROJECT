
def bank_app():

	balance = float(input("enter your balance: "))
	
	if balance < 100:
		print("enter higher balance : ")

while True:

	print("\n >>> semicolon Bank App>>>\n")
	
	print("enter 1 for withdrawal: ")

	print("enter 2 for transaction log: ")

	print("enter 3 to exist: ")

	user_select = input("select option: ")

	if user_select == '1':
	
		balance = float(input("enter your balance: "))
	
	if balance < 100:
		print("enter higher balance : ")

		amount = input("enter withdrawal fee: ")
		
		amount = 0.9 * balance		

		withdrawal_fee = 100

		total_withdrawal = amount + withdrawal_fee

	
		if amount < 0:

			print("Negative amount cannot be processed: ")

		else:
			if amount % 500 == 0:
		
				remaining_balance = balance - amount

		print("tranction succesful :")

		print(f" your balance is {balance}")

		print(f" withdrawal fee is {withdrawal_fee}")

		print(f" remaining balance is {remaining_balance}")

	
	#if user_select == '2':


	if user_select == '3':
		print("exist bank app")
	break;
		
bank_app()
	