from unittest import TestCase, main

from TESTING_lecture.car_manager.project.car_manager import Car


class CarManagerTest(TestCase):

    def setUp(self):
        self.car = Car("Lada", "S-line", 10, 99)

    def test_correct_initialization(self):
        self.assertEqual("Lada", self.car.make)
        self.assertEqual("S-line", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(99, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_raise_exception_empty_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_raise_exception_empty_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_raise_exception_zero_or_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = - 1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_raise_exception_zero_or_negative_fuel_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_raise_exception_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_raise_exception_refuel_with_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_fuel_more_than_fuel_capacity(self):
        self.car.refuel(999)
        self.assertEqual(99, self.car.fuel_amount)

    def test_correct_refuel(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_raise_exception_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_correct_driving_with_enough_fuel(self):
        self.car.fuel_amount = 10
        self.car.drive(10)
        self.assertEqual(9, self.car.fuel_amount)


if __name__ == "__main__":
    main()
