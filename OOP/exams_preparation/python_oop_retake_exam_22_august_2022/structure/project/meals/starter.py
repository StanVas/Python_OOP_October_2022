# from exams_preparation.python_oop_retake_exam_22_august_2022.structure.project.meals.meal import Meal
from decorators_09_not_done.project import Meal


class Starter(Meal):
    def __init__(self, name, price, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
