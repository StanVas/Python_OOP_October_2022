from exams_preparation.python_oop_retake_exam_18_april_2022.test.project.plantation import Plantation
# from project.plantation import Plantation

from unittest import TestCase, main



class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(5)

    def test_correct_initialization(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_raising_value_error_making_size_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            new_plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_correct_hire_worker_method(self):
        result = self.plantation.hire_worker('Gosho')
        self.assertEqual('Gosho successfully hired.', result)
        self.assertEqual(['Gosho'], self.plantation.workers)

    def test_raising_value_error_when_trying_to_hire_same_worker(self):
        self.plantation.workers.append('Gosho')
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Gosho')
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_correct__len__method(self):
        worker = 'Gosho'
        flowers = ['roses', 'orchids']
        self.plantation.plants[worker] = flowers
        result = self.plantation.__len__()
        self.assertEqual(2, result)

    def test_raising_value_error_cannot_find_worker_for_planting_func(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Gosho', 'rose')
        self.assertEqual("Worker with name Gosho is not hired!", str(ve.exception))

    def test_raising_value_error_when_plantation_is_full_planting_func(self):
        self.plantation.size = 0
        self.plantation.workers.append('Gosho')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Gosho', 'rose')
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_correct_planting_func_with_worker_already_in_workers_dict(self):
        self.plantation.workers.append('Gosho')
        self.plantation.plants['Gosho'] = ['orchid']
        result = self.plantation.planting('Gosho', 'rose')
        self.assertEqual('Gosho planted rose.', result)
        self.assertEqual(['orchid', 'rose'], self.plantation.plants['Gosho'])

    def test_correct_planting_func_with_worker_not_in_workers_dict(self):
        self.plantation.workers.append('Gosho')
        result = self.plantation.planting('Gosho', 'rose')
        self.assertEqual("Gosho planted it's first rose.", result)
        self.assertEqual(['rose'], self.plantation.plants['Gosho'])

    def test_correct__str__(self):
        self.plantation.workers.append('Gosho')
        self.plantation.plants['Gosho'] = ['rose']
        result = self.plantation.__str__()
        self.assertEqual("Plantation size: 5\nGosho\nGosho planted: rose", result)

    def test_correct__repr__(self):
        self.plantation.workers.append('Gosho')
        self.assertEqual("Size: 5\nWorkers: Gosho", self.plantation.__repr__())


if __name__ == '__main__':
    main()
