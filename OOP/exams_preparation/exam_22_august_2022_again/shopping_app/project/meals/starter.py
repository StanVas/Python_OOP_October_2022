from exams_preparation.exam_22_august_2022_again.shopping_app.project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name, price, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
