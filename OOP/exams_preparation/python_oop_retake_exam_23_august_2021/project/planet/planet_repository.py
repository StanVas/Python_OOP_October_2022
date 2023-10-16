# from exams_preparation.python_oop_retake_exam_23_august_2021.project.planet.planet import Planet
from decorators_09_not_done.project import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet
