from unittest import TestCase, main

from TESTING_lecture.worker.project.worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('Gosho', 777, 666)

    def test_correct_initializing(self):
        self.assertEqual("Gosho", self.worker.name)
        self.assertEqual(777, self.worker.salary)
        self.assertEqual(666, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_raise_exception_working_with_zero_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_energy_change_after_working(self):
        self.worker.work()
        self.assertEqual(665, self.worker.energy)

    def test_money_change_after_working(self):
        self.worker.work()
        self.assertEqual(777, self.worker.money)

    def test_rest_energy_change(self):
        self.worker.rest()
        self.assertEqual(667, self.worker.energy)

    def test_get_correct_info(self):
        self.assertEqual(f'Gosho has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
