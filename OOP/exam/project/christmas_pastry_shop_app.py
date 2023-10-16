from exam.project.booths.open_booth import OpenBooth
from exam.project.booths.private_booth import PrivateBooth
from exam.project.delicacies.gingerbread import Gingerbread
from exam.project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def find_delicacy(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        test_delicacy = self.find_delicacy(name)
        if test_delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        current_delicacy = None

        if type_delicacy == 'Gingerbread':
            current_delicacy = Gingerbread(name, price)

        elif type_delicacy == 'Stolen':
            current_delicacy = Stolen(name, price)

        self.delicacies.append(current_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def find_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        booth = self.find_booth(booth_number)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        current_booth = None

        if type_booth == "Open Booth":
            current_booth = OpenBooth(booth_number, capacity)

        elif type_booth == "Private Booth":
            current_booth = PrivateBooth(booth_number, capacity)

        self.booths.append(current_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        current_booth = None

        for booth in self.booths:
            if current_booth:
                break
            if not booth.is_reserved and booth.capacity >= number_of_people:
                current_booth = booth

        if not current_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        current_booth.reserve(number_of_people)
        return f"Booth {current_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_booth = self.find_booth(booth_number)
        current_delicacy = self.find_delicacy(delicacy_name)

        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = self.find_booth(booth_number)

        bill = 0
        bill += current_booth.price_for_reservation
        for delicacy in current_booth.delicacy_orders:
            bill += delicacy.price

        current_booth.delicacy_orders = []
        current_booth.price_for_reservation = 0
        current_booth.is_reserved = False
        self.income += bill

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
