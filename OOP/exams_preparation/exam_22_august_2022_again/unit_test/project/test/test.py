from exams_preparation.exam_22_august_2022_again.unit_test.project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shop = ShoppingCart('METRO', 200)
        self.shop.products['mayo'] = 1

    def test_correct_initialization(self):
        self.assertEqual('METRO', self.shop.shop_name)
        self.assertEqual(200, self.shop.budget)
        self.assertEqual({'mayo': 1}, self.shop.products)

    def test_initializing_name_without_capital_first_letter(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('mETRO', 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_initializing_name_with_numbers(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('M1TR1', 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_correct_add_to_cart_method(self):
        result = self.shop.add_to_cart('ketchup', 2)
        self.assertEqual({'mayo': 1, 'ketchup': 2}, self.shop.products)
        self.assertEqual("ketchup product was successfully added to the cart!", result)

    def test_incorrect_add_to_cart_with_price_more_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart('wine', 120)
        self.assertEqual("Product wine cost too much!", str(ve.exception))

    def test_correct_remove_method(self):
        self.shop.add_to_cart('ketchup', 2)
        result = self.shop.remove_from_cart('mayo')
        self.assertEqual({'ketchup': 2}, self.shop.products)
        self.assertEqual("Product mayo was successfully removed from the cart!", result)

    def test_incorrect_remove(self):
        self.shop.add_to_cart('ketchup', 2)
        with self.assertRaises(ValueError) as ve:
            result = self.shop.remove_from_cart('wine')
        self.assertEqual("No product with name wine in the cart!", str(ve.exception))
        self.assertEqual({'mayo': 1, 'ketchup': 2}, self.shop.products)

    def test__add__method_(self):
        shop2 = ShoppingCart('LIDL', 110)
        shop2.products['wine'] = 10

        new_shop = self.shop.__add__(shop2)
        self.assertEqual('METROLIDL', new_shop.shop_name)
        self.assertEqual(310, new_shop.budget)
        self.assertEqual({'mayo': 1, 'wine': 10}, new_shop.products)

    def test_correct_buy_products_method(self):
        self.shop.add_to_cart('ketchup', 2)
        self.shop.add_to_cart('wine', 7)
        result = self.shop.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 10.00lv.', result)

    def test_incorrect_buy_products(self):
        self.shop.add_to_cart('ketchup', 29)
        self.shop.add_to_cart('wine', 90)
        self.shop.add_to_cart('whiskey', 90)
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))


if __name__ == '__main__':
    main()
