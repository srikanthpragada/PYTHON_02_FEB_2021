class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def category(self):
        if self.age < 30:
            return "Young"
        elif self.age < 60:
            return "Middle-aged"
        else:
            return "Old"

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1 = Person("Mike", 30)  # p1.__init__('Mike',30)
print(p1.category)
p2 = Person("Mike", 30)
print(p1 == p2)
print(p1)  # str(p1) -> p1.__str__()

persons = [Person("Steve", 40), Person("James", 60), Person("Anders", 55)]

for p in sorted(persons):
    print(p)
