accounts = []

def create_account(name, phone_Number, balance):
	account = [name, phone_Number, balance]
	accounts.append(account)
	return "account"


def deposit_funds_into_account(name, amount, balance):
	amount = float(amount)
	if amount < 0:
		return None
	balance = balance + amount
	return balance
		

def withdraw(name, amount_to_be_withdrawn, balance):
	amount_to_be_withdrawn = float(amount_to_be_withdrawn)
	if amount_to_be_withdrawn < 0:
		return None
	balance = balance - amount_to_be_withdrawn 
	return balance 