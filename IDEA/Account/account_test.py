import unittest

import account #

class MyTestCase(unittest.TestCase):
    def test_deposit_is_correct(self):
        self.assertEqual(account.Account("TestAccount", 100).deposit(50), 150)
        self.assertEqual(account.Account("TestAccount", 900).deposit(50), 950)
        self.assertEqual(account.Account("TestAccount", 0).deposit(100), 100)


    def test_withdraw_is_correct(self):
        self.assertEqual(account.Account("TestAccount", 100).withdraw(50), 50)
        self.assertEqual(account.Account("TestAccount", 100).withdraw(100), 0)
        self.assertEqual(account.Account("TestAccount", 100).withdraw(150), "Insufficient funds")

    def test_initial_balance_is_correct(self):
        self.assertEqual(account.Account("TestAccount", 100).balance, 100)
        self.assertEqual(account.Account("TestAccount", 0).balance, 0)
        self.assertRaises(ValueError, account.Account, "TestAccount", -100)



if __name__ == '__main__':
    unittest.main()
