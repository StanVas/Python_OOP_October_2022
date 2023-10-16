# from project_06.wild_farm.project.animals.animal import Mammal
# from project_06.wild_farm.project.food import Meat, Vegetable, Fruit
from exams_preparation.exam_22_august_2022_again.unit_test.project import Mammal
from exams_preparation.exam_22_august_2022_again.unit_test.project import Meat, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1
