from exams_preparation.project.horse_race import HorseRace
from exams_preparation.project.horse_specification.appaloosa import Appaloosa
from exams_preparation.project.horse_specification.thoroughbred import Thoroughbred
from exams_preparation.project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __find_horse(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def __find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        horse_validation = self.__find_horse(horse_name)

        if horse_validation:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in ['Appaloosa', 'Thoroughbred']:
            return

        if horse_type == 'Appaloosa':
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

        elif horse_type == 'Thoroughbred':
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        jockey_validation = self.__find_jockey(jockey_name)

        if jockey_validation:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jockey = self.__find_jockey(jockey_name)

        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            current_horse = next(filter(lambda x: (type(x).__name__ == horse_type and not x.is_taken), reversed(self.horses)))
        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        # if not current_horse: # we have to use try: except: in this case
        #     raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        current_jockey.horse = current_horse
        current_horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        current_race = None

        for race in self.horse_races:
            if race.race_type == race_type:
                current_race = race

        if not current_race:
            raise Exception(f"Race {race_type} could not be found!")

        current_jockey = self.__find_jockey(jockey_name)

        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for jockey in current_race.jockeys:
            if jockey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        current_race = None

        for race in self.horse_races:
            if race.race_type == race_type:
                current_race = race

        if not current_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner = None

        for jockey in current_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is" \
               f" {winner.name}! Winner's horse: {winner.horse.name}."
