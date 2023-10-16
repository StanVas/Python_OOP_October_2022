class Client:
    def __init__(self, phone_num: str):
        self.phone_number = phone_num
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] != "0" or len(value) != 10 or not value.isnumeric():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
