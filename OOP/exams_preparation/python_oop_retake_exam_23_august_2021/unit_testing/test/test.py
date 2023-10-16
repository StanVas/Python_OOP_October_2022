from exams_preparation.python_oop_retake_exam_23_august_2021.unit_testing.project.library import Library
# from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library('Dr.Dre')
        self.library.books_by_authors = {'Greg Bear': ['EON']}
        self.library.readers = {'Gosho': []}

    def test_correct_initialization(self):
        self.new_library = Library('DR.DRE')
        self.assertEqual('DR.DRE', self.new_library.name)
        self.assertEqual({}, self.new_library.books_by_authors)
        self.assertEqual({}, self.new_library.readers)

    def test_name_setter_raising_value_error_for_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_correctly_if_author_not_in_books_by_authors(self):
        self.library.add_book('George Orwell', "1984")
        self.assertEqual({'Greg Bear': ['EON'], 'George Orwell': ['1984']}, self.library.books_by_authors)

    def test_add_book_correctly_if_author_in_books_by_authors(self):
        self.library.add_book('Greg Bear', 'Eternity')
        self.assertEqual({'Greg Bear': ['EON', 'Eternity']}, self.library.books_by_authors)

    def test_add_reader_if_reader_not_in_readers_list(self):
        self.library.add_reader('Ivan')
        self.assertEqual({'Gosho': [], 'Ivan': []}, self.library.readers)

    def test_return_message_if_trying_to_add_reader_that_exists(self):
        result = self.library.add_reader('Gosho')
        self.assertEqual("Gosho is already registered in the Dr.Dre library.", result)
        self.assertEqual({'Gosho': []}, self.library.readers)

    def test_rent_book_if_reader_not_in_self_readers(self):
        result = self.library.rent_book('Pesho', 'Greg Bear', 'EON')
        self.assertEqual("Pesho is not registered in the Dr.Dre Library.", result)

    def test_rent_book_if_author_not_in_books_by_authors(self):
        result = self.library.rent_book('Gosho', 'G.Bear', 'EON')
        self.assertEqual("Dr.Dre Library does not have any G.Bear's books.", result)

    def test_rent_book_if_title_not_in_books_by_authors(self):
        result = self.library.rent_book('Gosho', 'Greg Bear', 'Eternity')
        self.assertEqual("""Dr.Dre Library does not have Greg Bear's "Eternity".""", result)

    def test_correct_rent_book(self):
        self.library.add_book('George Orwell', "1984")
        self.library.rent_book('Gosho', 'Greg Bear', 'EON')
        self.assertEqual({'Gosho': [{'Greg Bear': 'EON'}]}, self.library.readers)
        self.assertEqual({'Greg Bear': [], 'George Orwell': ['1984']}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
