class Student:
    # static or class attributes
    courses = {'python': 5000, 'ds': 10000, 'django': 3000}

    @staticmethod
    def get_course_fee(course):
        """
        Returns course fee for given course. None if course is not found.
        """
        if course in Student.courses:
            return Student.courses[course]
        else:
            return None

    def __init__(self, admno, name, course='python'):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    def pay(self, amount):
        self.feepaid += amount

    def get_total_fee(self):
        return Student.courses[self.course]

    def get_due(self):
        return self.get_total_fee() - self.feepaid


print(Student.get_course_fee('java'))

s = Student(1, 'James', 'ds')
s.pay(5000)
s.get_course_fee('java')
print(s.get_due())
