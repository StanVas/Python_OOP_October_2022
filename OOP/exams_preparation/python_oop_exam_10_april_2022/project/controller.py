from exams_preparation.python_oop_exam_10_april_2022.project.player import Player
from exams_preparation.python_oop_exam_10_april_2022.project.supply.drink import Drink
from exams_preparation.python_oop_exam_10_april_2022.project.supply.food import Food


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        successfully_added = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                successfully_added.append(player.name)

        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    # def find_supply(self, supply_name):  # not working correctly !!!
    #     result = reversed([s for s in self.supplies if s.__class__.__name__ == supply_name])
    #     return result
    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        if not self.find_player(player_name):
            return

        player = self.find_player(player_name)

        if sustenance_type != 'Drink' and sustenance_type != 'Food':
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply = self.__take_last_supply(sustenance_type)
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        return f"{player_name} sustained successfully with {supply.name}."
        # if sustenance_type == 'Drink':  # part of find supply method
        #     if not self.find_supply(sustenance_type):
        #         return "There are no drink supplies left!"
        #
        # elif sustenance_type == 'Food':
        #     if not self.find_supply(sustenance_type):
        #         return "There are no food supplies left!"
        #
        # supply = self.find_supply(sustenance_type)
        # self.supplies.remove(supply)
        #
        # if player.stamina + supply.energy > 100:
        #     player.stamina = 100
        # else:
        #     player.stamina += supply.energy
        #
        # return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_pl = self.find_player(first_player_name)
        second_pl = self.find_player(second_player_name)

        result_in_case_zero_stamina = []
        if first_pl.stamina == 0:
            result_in_case_zero_stamina.append(f"Player {first_player_name} does not have enough stamina.")

        if second_pl.stamina == 0:
            result_in_case_zero_stamina.append(f"Player {second_player_name} does not have enough stamina.")

        if len(result_in_case_zero_stamina) != 0:
            return '\n'.join(result_in_case_zero_stamina)

        if first_pl.stamina < second_pl.stamina:
            damage = first_pl.stamina / 2
            second_pl.stamina -= damage

            if second_pl.stamina < 0:
                second_pl.stamina = 0
                return f"Winner: {first_player_name}"

            damage = second_pl.stamina / 2
            first_pl.stamina -= damage

            if first_pl.stamina < 0:
                first_pl.stamina = 0
                return f"Winner: {second_player_name}"

        elif first_pl.stamina > second_pl.stamina:
            damage = second_pl.stamina / 2
            first_pl.stamina -= damage

            if first_pl.stamina < 0:
                first_pl.stamina = 0
                return f"Winner: {second_player_name}"

            damage = first_pl.stamina / 2
            second_pl.stamina -= damage

            if second_pl.stamina < 0:
                second_pl.stamina = 0
                return f"Winner: {first_player_name}"

        winner = first_player_name if first_pl.stamina > second_pl.stamina else second_player_name
        return f"Winner: {winner}"

    def next_day(self):
        for player in self.players:
            damage = player.age * 2

            if player.stamina - damage < 0:
                player.stamina = 0
            else:
                player.stamina -= damage

            # food_supply = self.find_supply('Food')  # removed find_supply
            food_supply = self.__take_last_supply('Food')
            # self.supplies.remove(food_supply) # removed find_supply

            if player.stamina + food_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += food_supply.energy

            # drink_supply = self.find_supply('Drink')  # removed find_supply
            drink_supply = self.__take_last_supply('Drink')
            # self.supplies.remove(drink_supply)    # removed find_supply

            if player.stamina + drink_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += drink_supply.energy

    def __str__(self):
        result = []
        for p in self.players:
            sustenance = True if p.need_sustenance else False
            result.append(f"Player: {p.name}, {p.age}, {p.stamina}, {sustenance}")
        for s in self.supplies:
            result.append(s.details())
        return '\n'.join(result)


controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
