import unittest
import bank_app

class TestBank(unittest.TestCase):
	def test_account_function_exist(self):
		bank_app.create_account("theophilus", "8104116411" , 100)
		
	def test_account_created(self):
		account = bank_app.create_account("theophilus", "8104116411", 100)
		self.assertEqual(account, "account")
	
	def test_phone_number_has_to_be_10_degits(self):
		account = ["theophilus", "8104116411", 100]
		phone_number = account[1]
		result = len(phone_number)
		self.assertEqual(result, 10)


	def test_phone_number_is_not_negative(self):
		account = ["theophilus", "8104116411", 100]
		phone_number = int(account[1])
		self.assertGreaterEqual(phone_number, 0)

		
	def test_account_balance_is_not_negative(self):
		account = ["theophilus", "8104116411", 100]
		balance = int(account[2])
		self.assertGreaterEqual(balance, 0)
	
		
	def test_account_name_is_contains_letters_no_symbols_or_digits(self):
		account = ["theophilus", "8104116411", 100]
		name = account[0]
		self.assertTrue(name.isalpha()) 

	def find_account(phone_number):
		for account in accounts:
			if account[1] == phone_number:
				return account
		raise ValueError("Account not found")


	def test_phone_number_identify(self):
		account = ["theophilus", "8104116411", 100]
		phone_number = account[1]
		self.assertEqual( phone_number, "8104116411" )

	

	def test_account_name_identity(self):
		account = ["theophilus", "8104116411", 100]
		name = account[0]
		self.assertEqual(name ,"theophilus")


	def test_that_deposit_function_exists(self):
		bank_app.deposit_funds_into_account("theophilus", 1000, 100)
	
	def test_you_can_deposit_amount_in_decimal(self):
		actual = ("theophilus", 500.5, 1500)

	def test_deposit_amount_is_not_negative(self):
		bank_app.create_account("theophilus", -1000, 2000)
	


	def test_that_withdraw_function_exists(self):
		bank_app.withdraw("theophilus", 500 , 2000)

	def test_withdraw_function_is_not_negative(self):
		bank_app.create_account("theophilus", -1000, 2000)
			
	def test_you_can_withdraw(self):
		actual = ("theophilus", 500 , 1500)
				
		
	def test_you_can_withdraw_amount_in_decimal(self):
		actual = ("theophilus", 500.5, 1500)
		