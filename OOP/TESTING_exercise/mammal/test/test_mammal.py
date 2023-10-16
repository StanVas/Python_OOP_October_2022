from unittest import TestCase, main

from TESTING_exercise.mammal.project.mammal import Mammal
# from project.mammal import Mammal


class MammalTest(TestCase):

    def setUp(self):
        self.animal = Mammal("Germundo", "bear", "brum brum")

    def test_correct_initialization(self):
        self.assertEqual('Germundo', self.animal.name)
        self.assertEqual('bear', self.animal.type)
        self.assertEqual('brum brum', self.animal.sound)
        self.assertEqual('animals', self.animal._Mammal__kingdom)

    def test_correct_message_make_sound(self):
        result = self.animal.make_sound()
        self.assertEqual("Germundo makes brum brum", result)

    def test_correct_get_kingdom_output(self):
        result = self.animal.get_kingdom()
        self.assertEqual('animals', result)

    def test_correct_message_info(self):
        result = self.animal.info()
        self.assertEqual('Germundo is of type bear', result)


if __name__ == '__main__':
    main()
