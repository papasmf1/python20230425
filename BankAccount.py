
class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, 
            self.name, self.balance)


account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)


