from unittest import TestCase, main

from TESTING_lecture.list.project.integer_list import IntegerList


class IntegerListTest(TestCase):

    def setUp(self):
        self.integer_list = IntegerList("10", 1, "str", 2, False, 3, 6.4)

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_not_correct_type_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('asdf')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_correct_append_element(self):
        self.integer_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.integer_list._IntegerList__data)

    #TODO

    def test_remove_index_with_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(99)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_delete_element(self):
        self.integer_list.remove_index(0)

        self.assertEqual([2, 3], self.integer_list.get_data())

    def test_get_with_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(99)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index(self):
        result = self.integer_list.get(1)

        self.assertEqual(2, result)

    def test_insert_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(99, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_invalid_element_type(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, "gosho")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_command(self):
        self.integer_list.insert(0, 9)

        self.assertEqual([9, 1, 2, 3], self.integer_list.get_data())

    def test_get_biggest(self):
        result = self.integer_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.integer_list.get_index(3)

        self.assertEqual(2, result)


if __name__ == '__main__':
    main()
