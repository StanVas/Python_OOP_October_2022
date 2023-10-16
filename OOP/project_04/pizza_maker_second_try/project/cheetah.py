from project_04.pizza_maker_second_try.project.animal import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.MONEY_FOR_CARE)
