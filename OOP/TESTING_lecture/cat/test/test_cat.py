from unittest import TestCase, main

from TESTING_lecture.cat.project.cat import Cat


class CatTest(TestCase):

    def setUp(self):
        self.cat = Cat('Sharo')

    def test_correct_initialization(self):
        self.assertEqual('Sharo', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_catch_exception_eating_when_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_valid_cat_eating(self):
        self.cat.eat()

        self.assertEqual(True, self.cat.fed)

        self.assertEqual(True, self.cat.sleepy)

        self.assertEqual(1, self.cat.size)

    def test_sleep_raise_exception_while_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
