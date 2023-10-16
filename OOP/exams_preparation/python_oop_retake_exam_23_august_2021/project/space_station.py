# from exams_preparation.python_oop_retake_exam_23_august_2021.project.astronaut.astronaut_repository import \
#     AstronautRepository
# from exams_preparation.python_oop_retake_exam_23_august_2021.project.planet.planet_repository import PlanetRepository
# from exams_preparation.python_oop_retake_exam_23_august_2021.project.astronaut.biologist import Biologist
# from exams_preparation.python_oop_retake_exam_23_august_2021.project.astronaut.geodesist import Geodesist
# from exams_preparation.python_oop_retake_exam_23_august_2021.project.astronaut.meteorologist import Meteorologist
# from exams_preparation.python_oop_retake_exam_23_august_2021.project.planet.planet import Planet
# from project.planet.planet_repository import PlanetRepository
# from project.astronaut.astronaut_repository import AstronautRepository
# form project.astronaut.biologist import Biologist
# form project.astronaut.biologist import Geodesist
# form project.astronaut.biologist import Meteorologist
# from project.planet.planet import Planet


class SpaceStation:
    successful_missions = 0
    not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type != "Biologist" and astronaut_type != "Geodesist" and astronaut_type != "Meteorologist":
            return "Astronaut type is not valid!"

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."

        if astronaut_type == 'Biologist':
            astronautt = Biologist(name)
            self.astronaut_repository.astronauts.append(astronautt)

        elif astronaut_type == 'Geodesist':
            astronautt = Geodesist(name)
            self.astronaut_repository.astronauts.append(astronautt)

        elif astronaut_type == 'Meteorologist':
            astronautt = Meteorologist(name)
            self.astronaut_repository.astronauts.append(astronautt)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):   # separated with ', ' so maybe *args
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."

        planet = Planet(name)
        planet.items.append(items)
        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remove(name)
                return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        condition = False
        current_planet = object
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                current_planet = planet
                condition = True

        if not condition:
            raise Exception("Invalid planet name!")

        highest_oxygen = sorted([a for a in self.astronaut_repository.astronauts], key=lambda x: (-x.oxygen))
        chosen_astronauts = []

        for astro in highest_oxygen:
            if astro.oxygen <= 30:
                highest_oxygen.remove(astro)

        if len(highest_oxygen) == 0:
            return "You need at least one astronaut to explore the planet!"

        if len(highest_oxygen) > 5:
            for i in range(5):
                chosen_astronauts.append(highest_oxygen[i])
        else:
            for i in range(len(highest_oxygen)):
                chosen_astronauts.append(highest_oxygen[i])

        chosen_astronauts_names = [a.name for a in chosen_astronauts]

        while True:
            if len(current_planet.items) == 0:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. {', '.join(chosen_astronauts_names)} astronauts participated in collecting items."

            if len(chosen_astronauts) == 0:
                self.not_completed_missions += 1
                return "Mission is not completed."

            current_astronaut = chosen_astronauts[0]
            item = current_planet.items.pop()
            current_astronaut.backpack.append(item)
            current_astronaut.breathe()
            if current_astronaut.oxygen <= 0:
                chosen_astronauts.remove(current_astronaut)

            continue

    def report(self):
        result = [
            f'{self.successful_missions} successful missions!',
            f'{self.not_completed_missions} missions were not completed!',
            f"Astronauts' info:",
        ]

        for astro in self.astronaut_repository.astronauts:
            result.append(f'Name: {astro.name}')
            result.append(f'Oxygen: {astro.oxygen}')
            if len(astro.backpack) == 0:
                result.append(f'Backpack items: {"none"}')
            else:
                result.append(f"Backpack items: {', '.join(astro.backpack)}")

        return '\n'.join(result)


# space_station = SpaceStation()
# astronaut1 = SpaceStation.add_astronaut(space_station, 'Biologist', 'Gosho')
# # astronaut4 = SpaceStation.add_astronaut(space_station, 'Biologist', 'asdada')
# # astronaut5 = SpaceStation.add_astronaut(space_station, 'Biologist', 'Gosadfsdfsdfho')
# # astronaut6 = SpaceStation.add_astronaut(space_station, 'Biologist', '1111Gosadfsdfsdfho')
# astronaut2 = SpaceStation.add_astronaut(space_station, 'Geodesist', 'Ivan')
# astronaut3 = SpaceStation.add_astronaut(space_station, 'Meteorologist', 'Pesho')
# planet1 = SpaceStation.add_planet(space_station, 'Mars', 'kirka')
# print(space_station.send_on_mission('Mars'))
# print(space_station.report())
