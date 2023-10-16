from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()
        self.toy_store.toy_shelf['A'] = 'teddy bear'

    def test_correct_initialization(self):
        self.assertEqual({'A': 'teddy bear', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}, self.toy_store.toy_shelf)

    def test_incorrect_add_toy_with_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('Z', 'cycle')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_incorrect_add_toy_with_toy_already_added(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'teddy bear')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_incorrect_add_toy_with_shelf_already_taken(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'cycle')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_correct_add_toy(self):
        result = self.toy_store.add_toy('B', 'cycle')
        self.assertEqual("Toy:cycle placed successfully!", result)
        self.assertEqual({'A': 'teddy bear', 'B': 'cycle', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_incorrect_remove_toy_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('Z', 'cycle')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_incorrect_remove_toy_toy_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'cycle')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_correct_remove_toy(self):
        self.toy_store.add_toy('B', 'cycle')
        result = self.toy_store.remove_toy('A', 'teddy bear')
        self.assertEqual("Remove toy:teddy bear successfully!", result)
        self.assertEqual({'A': None, 'B': 'cycle', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)


if __name__ == '__main__':
    main()
