from project_04.pizza_maker_second_try.project.animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.MONEY_FOR_CARE)