# from exams_preparation.python_oop_exam_11_december_2021.project.car.muscle_car import MuscleCar
# from exams_preparation.python_oop_exam_11_december_2021.project.car.sports_car import SportsCar
# from exams_preparation.python_oop_exam_11_december_2021.project.driver import Driver
# from exams_preparation.python_oop_exam_11_december_2021.project.race import Race
from decorators_09_not_done.project import MuscleCar
from decorators_09_not_done.project import SportsCar
from decorators_09_not_done.project import Driver
from decorators_09_not_done.project import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def check_for_car(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                return True
        return False

    def check_for_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True
        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type != 'MuscleCar' and car_type != 'SportsCar':
            return

        car = self.check_for_car(model)
        if car:
            raise Exception(f"Car {model} is already created!")

        if car_type == 'MuscleCar':
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
        elif car_type == 'SportsCar':
            car = SportsCar(model, speed_limit)
            self.cars.append(car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.check_for_driver(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def __find_car_type(self, car_type):
        for i in range(len(self.cars), 0, - 1):
            if type(self.cars[i - 1]).__name__ == car_type:
                return self.cars.pop(i - 1)
        if car_type == 'MuscleCar':
            raise Exception(f"Car {car_type} could not be found!")
        if car_type == 'SportsCar':
            raise Exception(f"Car {car_type} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.check_for_driver(driver_name)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type != 'MuscleCar' and car_type != 'SportsCar':
            return

        current_driver = [d for d in self.drivers if d.name == driver_name][0]
        current_car = self.__find_car_type(car_type)

        if not current_car:
            return f"Car {car_type} could not be found!"

        if current_car.is_taken:
            return

        if current_driver.car:
            old_car = current_driver.car
            old_car.is_taken = False
            self.cars.append(old_car)
            current_driver.car = current_car
            current_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {current_car.model}."

        if not current_driver.car:
            current_driver.car = current_car
            current_car.is_taken = True
            return f"Driver {driver_name} chose the car {current_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_race = None
        for race in self.races:
            if race.name == race_name:
                current_race = race
        if current_race is None:
            raise Exception(f"Race {race_name} could not be found!")

        current_driver = None
        for driver in self.drivers:
            if driver.name == driver_name:
                current_driver = driver
        if current_driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for driver in current_race.drivers:
            if driver.name == current_driver.name:
                raise Exception(f"Driver {driver_name} is already added in {race_name} race.")

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_race = None
        for race in self.races:
            if race.name == race_name:
                current_race = race

        if current_race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = sorted([d for d in current_race.drivers], key=lambda x: (-x.car.speed_limit))
        output = []
        for i in range(3):
            driver = result.pop(0)
            output.append(driver)
            driver.number_of_wins += 1

        return_output = []

        for driver in output:
            return_output.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(return_output)
