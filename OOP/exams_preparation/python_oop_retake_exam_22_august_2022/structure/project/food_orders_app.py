# from exams_preparation.python_oop_retake_exam_22_august_2022.structure.project.client import Client
from decorators_09_not_done.project import Client
# from exams_preparation.python_oop_retake_exam_22_august_2022.structure.project.meals.starter import Starter
# from exams_preparation.python_oop_retake_exam_22_august_2022.structure.project.meals.dessert import Dessert
# from exams_preparation.python_oop_retake_exam_22_august_2022.structure.project.meals.main_dish import MainDish
# from exams_preparation.python_oop_retake_exam_22_august_2022.structure.project.meals.meal import Meal


class FoodOrdersApp:
    POSSIBLE_DISHES = [
        'Starter',
        'MainDish',
        'Dessert'
    ]
    RECEIPT_COUNTER = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")  # TODO(return or raise?)
        except StopIteration:
            pass

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in self.POSSIBLE_DISHES:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for dish in self.menu:
            print(dish.details())  # maybe return

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            # TODO
        for meal_name in meal_names_and_quantities:
            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))
            except StopIteration:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal_names_and_quantities[meal_name] > meal.quantity:
                raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")

        for meal_name in meal_names_and_quantities:
            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))
            except StopIteration:
                pass
            client.shopping_cart.append(meal_name)
            client.bill += meal.price * meal_names_and_quantities[meal_name]

        return f"Client {client_phone_number} successfully ordered {', '.join(client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            pass
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        client.shopping_cart = []
        client.bill = 0

    def finish_order(self, client_phone_number: str):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            pass
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        self.RECEIPT_COUNTER += 1
        client.shopping_cart = []
        current_bill = client.bill
        client.bill = 0
        return f"Receipt #{self.RECEIPT_COUNTER - 1} with total amount of {current_bill:.2f} was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {self.RECEIPT_COUNTER - 1} clients."


# food_orders_app = FoodOrdersApp()
# print(food_orders_app.register_client("0899999999"))
# french_toast = Starter("French toast", 6.50, 5)
# hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
# tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
# risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
# chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
# chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
# print(food_orders_app.add_meals_to_menu(
#     french_toast, hummus_and_avocado_sandwich,
#     tortilla_with_beef_and_pork,
#     risotto_with_wild_mushrooms,
#     chocolate_cake_with_mascarpone,
#     chocolate_and_violets))
# print(food_orders_app.show_menu())
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)
