class BalanceError(Exception):
    def __init__(self, balance, amount):
        self.message = f"Available balance is {balance}, but you want to withdraw {amount}"

    def __str__(self):
        return self.message


class Account:
    minbal = 10000

    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        # Private attribute
        self.__balance = balance

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise BalanceError(self.__balance, amount)

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Steve", 20000)
a2 = Account(2, "Mike")
a1.deposit(10000)
try:
    a1.withdraw(50000)
except Exception  as ex:
    print(ex)

# a1._Account__balance = 10000000
print(a1.__dict__)
print(a1.acno, a1.ahname, a1.getbalance())
