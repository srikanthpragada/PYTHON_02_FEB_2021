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
            print("Insufficient Funds!")

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Steve", 20000)
a2 = Account(2, "Mike")
a1.deposit(10000)
a1.withdraw(50000)
#a1._Account__balance = 10000000
print(a1.__dict__)
print(a1.acno, a1.ahname, a1.getbalance())
