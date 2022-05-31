class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account


    def withdraw(self,subtracts):
        if self.balance < subtracts:
            raise ValueError(f"{self.name} can't withdraw {subtracts}, he only has {self.balance}.")
        self.balance -= subtracts
        return f"{self.name} has {self.balance}."


    def check(self,sender, refill):
        if sender.balance < refill or not sender.checking_account:
            raise ValueError
        self.balance += refill
        sender.balance -= refill
        return f'{self.name} has {self.balance} and {sender.name} has {sender.balance}.'


    def add_cash(self, refill):
        self.balance += refill
        return f'{self.name} has {int(self.balance)}.'


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

print(Jeff.withdraw(2)) # Returns 'Jeff has 68.'

print(Joe.check(Jeff, 50)) # Returns 'Joe has 120 and Jeff has 18.'

print(Jeff.check(Joe, 80)) # Raises a ValueError

print(Joe.checking_account == True) # Enables checking for Joe

print(Jeff.check(Joe, 80)) # Returns 'Jeff has 98 and Joe has 40'

print(Joe.check(Jeff, 100)) # Raises a ValueError

print(Jeff.add_cash(20.00)) # Returns 'Jeff has 118.'