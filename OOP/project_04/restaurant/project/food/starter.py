from project_04.restaurant.project.food.food import Food


class Starter(Food):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)
