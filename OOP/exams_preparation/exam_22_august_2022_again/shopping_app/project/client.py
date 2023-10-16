class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.quantities = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        # if len(value) != 10 or value[0] != '0':
        #     raise ValueError("Invalid phone number!")
        # for ch in value:
        #     if not ch.isdigit():
        #         raise ValueError("Invalid phone number!")
        # self.__phone_number = value
        if len(value) == 10 and value[0] == '0' and value.isdigit():
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")
