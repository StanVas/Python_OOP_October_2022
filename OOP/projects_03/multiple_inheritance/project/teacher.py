from projects_03.multiple_inheritance.project.employee import Employee
from projects_03.multiple_inheritance.project.person import Person
# from project.employee import Employee
# from project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
