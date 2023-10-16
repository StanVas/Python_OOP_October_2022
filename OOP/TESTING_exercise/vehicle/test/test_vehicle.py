from unittest import TestCase

# from TESTING_exercise.vehicle.project.vehicle import Vehicle
from decorators_09_not_done.project import Vehicle


class VehicleTest(TestCase):

    def setUp(self):
        self.car = Vehicle(50, 100)

    def test_correct_initialization(self):
        self.assertEqual(50, self.car.fuel)
        self.assertEqual(50, self.car.capacity)
        self.assertEqual(100, self.car.horse_power)
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_raise_exception_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel = 1
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_correct_driving_decrease_fuel(self):
        self.car.drive(10)
        self.assertEqual(37.5, self.car.fuel)

    def test_raise_exception_more_fuel_than_capacity_refuel_func(self):
        with self.assertRaises(Exception) as ex:
            result = self.car.refuel(999)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_refuel_and_fuel_increase(self):
        self.car.fuel = 40
        self.car.refuel(10)
        self.assertEqual(50, self.car.fuel)

    def test_correct_message_from__str__func(self):
        result = self.car.__str__()
        self.assertEqual("The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption", result)
