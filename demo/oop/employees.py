from abc import ABC, abstractmethod


# Abstract class
class Employee(ABC):
    def __init__(self, id, name, desg):
        self.id = id
        self.name = name
        self.desg = desg

    def __str__(self):
        return f"{self.id} - {self.name} - {self.desg}"

    @abstractmethod
    def get_salary(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, id, name, desg, salary):
        super().__init__(id, name, desg)
        self.salary = salary

    def __str__(self):  # Overriding
        return f"{super().__str__()} - {self.salary}"

    def get_salary(self):
        return self.salary


class Consultant(Employee):
    pass


s = SalariedEmployee(1, "Jack", "Programmer", 500000)
print(s)
