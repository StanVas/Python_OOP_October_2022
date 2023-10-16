from exams_preparation.python_oop_exam_10_april_2022.unit_testing.project.movie import Movie
# from project.movie import Movie

from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie('Alien', 1979, 8.5)

    def test_correct_initialization(self):
        self.assertEqual('Alien', self.movie.name)
        self.assertEqual(1979, self.movie.year)
        self.assertEqual(8.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_raising_value_error_with_incorrect_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_raising_value_error_with_incorrect_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1555
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_correct_add_actor_method(self):
        self.movie.add_actor('Brad Pit')
        self.assertEqual(['Brad Pit'], self.movie.actors)

    def test_add_actor_with_actor_already_in_the_list(self):
        self.movie.add_actor('Shkumbata')
        result = self.movie.add_actor('Shkumbata')
        self.assertEqual("Shkumbata is already added in the list of actors!", result)

    def test__gt__wiht_other_higher_rating(self):
        second_movie = Movie('The Godfather', 1972, 9.2)
        result = self.movie.__gt__(second_movie)
        self.assertEqual('"The Godfather" is better than "Alien"', result)

    def test__gt__wiht_other_lower_rating(self):
        second_movie = Movie('The Terminator', 1984, 8.1)
        result = self.movie.__gt__(second_movie)
        self.assertEqual('"Alien" is better than "The Terminator"', result)

    def test_correct__repr__method(self):
        self.movie.actors.append('Brad Pit')
        result = self.movie.__repr__()
        self.assertEqual("Name: Alien\nYear of Release: 1979\nRating: 8.50\nCast: Brad Pit", result)


if __name__ == '__main__':
    main()
