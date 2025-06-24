import bank_simulation_app

from unittest import TestCase

class Testlargest(TestCase):

	"""
	def test_check_dat_function_exist(self):

		bank_simulation_app.bank_app()
		"""
		
	
	def test_check_for_negative_amount(self):

		actual = bank_simulation_app.bank_app(-500)
		
		expected = -500
	
	self.assertEquals(actual, expected)
	

