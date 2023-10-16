# from project_06.wild_farm.project.animals.animal import Bird
# from project_06.wild_farm.project.food import Meat, Vegetable, Fruit, Seed
from exams_preparation.exam_22_august_2022_again.unit_test.project import Bird
from exams_preparation.exam_22_august_2022_again.unit_test.project import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35
