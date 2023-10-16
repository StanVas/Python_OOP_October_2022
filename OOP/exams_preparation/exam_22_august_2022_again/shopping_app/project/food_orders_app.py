from exams_preparation.exam_22_august_2022_again.shopping_app.project.client import Client


class FoodOrdersApp:
    receipt = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        current_client = Client(client_phone_number)
        self.clients_list.append(current_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:

            if meal.__class__.__name__ == "Starter" or meal.__class__.__name__ == "MainDish" \
                    or meal.__class__.__name__ == "Dessert":
                self.menu.append(meal)
            # if type(meal).__name__ in ['Starter', 'MainDish', 'Dessert']

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join([m.details() for m in self.menu])

    def find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    # def __find_meal(self, meal_name): # better make it private method
    #     for meal in self.menu:
    #         if meal.name == meal_name:
    #             return meal


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        current_client = None

        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client

        if not current_client:
            self.register_client(client_phone_number)
            for client in self.clients_list:
                if client.phone_number == client_phone_number:
                    current_client = client

        # for meal_name, meal_quantity in meal_names_and_quantities.items():  # only validations here
        #     if not self.__find_meal(meal_name):
        #         raise Exception(f"{meal_name} is not on the menu")
        #     current_meal = self.__find_meal(meal_name)
        #     if current_meal.quantity < meal_quantity:
        #         raise Exception(f'Not enough quantity of {type(current_meal).__name__}: {current_meal.name}!')

        ### if we got here no exception was raised so we are free to make changes with the objects
        # for meal_name, meal_quantity in meal_names_and_quantities.items():
        #     current_client.shopping_cart.append(current_meal)
        #     current_client.bill += current_meal.price * meal_quantity
        #     current_meal.quantity -= meal_quantity                         # decrease object quantity

        for meal in meal_names_and_quantities:
            if meal not in [m.name for m in self.menu]:
                raise Exception(f"{meal} is not on the menu!")

        for meal in meal_names_and_quantities:
            current_meal = self.find_meal(meal)
            if current_meal.quantity < meal_names_and_quantities[meal]:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {current_meal.name}!")

        for meal in meal_names_and_quantities:
            current_meal = self.find_meal(meal)
            if meal not in current_client.quantities:
                current_client.quantities[meal] = 0
            current_client.quantities[meal] += meal_names_and_quantities[meal]
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * meal_names_and_quantities[meal]
            for menu_meal in self.menu:
                if menu_meal.name == current_meal.name:
                    menu_meal.quantity -= meal_names_and_quantities[current_meal.name]

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([m.name for m in current_client.shopping_cart])} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client

        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for name, quantity in current_client.quantities.items():
            current_meal = self.find_meal(name)
            current_meal.quantity += quantity

        current_client.quantities.clear()
        current_client.shopping_cart.clear()
        current_client.bill = 0
        return f"Client {current_client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client

        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.receipt += 1
        bill = current_client.bill
        current_client.bill = 0
        current_client.shopping_cart.clear()
        current_client.quantities.clear()

        return f"Receipt #{self.receipt} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
