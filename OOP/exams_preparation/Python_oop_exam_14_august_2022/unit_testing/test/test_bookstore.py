from unittest import TestCase, main
from decorators_09_not_done.project import Bookstore
# from exams_preparation.Python_oop_exam_14_august_2022.unit_testing.project.bookstore import Bookstore


class BookstoreTest(TestCase):

    def setUp(self):
        self.bookstore = Bookstore(15)

    def test_correct_initialization(self):
        self.assertEqual(15, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_raise_value_error_less_or_equal_to_zero_books_limit(self):
        with self.assertRaises(ValueError) as ve:
            Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_correct_count_books_method(self):
        self.bookstore.availability_in_store_by_book_titles['Harry Potter'] = 6
        self.bookstore.availability_in_store_by_book_titles['Lord of the rings'] = 5
        result = self.bookstore.__len__()
        self.assertEqual(11, result)

    def test_raise_exception_extending_books_limit_with_receive_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Harry Potter', 100)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_correct_receiving_book_method_with_existing_book(self):  # two different methods catching both cases
        self.bookstore.receive_book('Harry Potter', 10)
        result = self.bookstore.receive_book('Harry Potter', 1)
        self.assertEqual("11 copies of Harry Potter are available in the bookstore.", result)

    def test_correct_receiving_book_method_with_new_book(self):     # two different methods catching both cases
        result = self.bookstore.receive_book('Harry Potter', 10)
        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles['Harry Potter'])
        self.assertEqual({'Harry Potter': 10}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("10 copies of Harry Potter are available in the bookstore.", result)

    def test_raise_exception_sell_book_with_not_available_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Harry Potter', 1)
        self.assertEqual("Book Harry Potter doesn't exist!", str(ex.exception))

    def test_raise_exception_sell_book_with_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles['Harry Potter'] = 5

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Harry Potter', 6)

        self.assertEqual("Harry Potter has not enough copies to sell. Left: 5", str(ex.exception))

    def test_correct_sell_book_method(self):
        self.bookstore.availability_in_store_by_book_titles['Harry Potter'] = 5

        result = self.bookstore.sell_book('Harry Potter', 5)

        self.assertEqual({'Harry Potter': 0}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bookstore.total_sold_books)
        self.assertEqual("Sold 5 copies of Harry Potter", result)

    def test__str__method(self):
        self.bookstore.receive_book('Harry Potter', 10)
        self.bookstore.sell_book('Harry Potter', 5)
        self.assertEqual(
            "Total sold books: 5\n"
            "Current availability: 5\n"
            " - Harry Potter: 5 copies",
            self.bookstore.__str__()
        )


if __name__ == '__main__':
    main()
