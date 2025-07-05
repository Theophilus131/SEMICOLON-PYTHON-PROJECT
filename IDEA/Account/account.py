
class Account:
    def __init__(self,name, balance= 0):
        self.name = name
        self.balance = balance
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
           return self.balance - amount

    def deposit(self, amount):
        self.balance += amount

        return self.balance


oba = Account("OBA", 1000)
print(oba.balance)

