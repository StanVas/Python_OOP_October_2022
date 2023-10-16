from unittest import TestCase, main

# from exams_preparation.python_oop_retake_exam_22_august_2022.unit_testing.project.shopping_cart import ShoppingCart
from decorators_09_not_done.project import ShoppingCart


class ShoppingCartTest(TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart('Metro', 100.0)
        self.second_shopping_cart = ShoppingCart('LIDL', 50.0)

    def test_correct_initialization(self):
        self.assertEqual('Metro', self.shopping_cart.shop_name)
        self.assertEqual(100.0, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_raise_value_error_in_setter_for_small_first_letter_in_shop_name(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('metro', 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_raise_value_error_in_setter_for_number_in_shop_name(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('Metro2', 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_raise_value_error_if_product_price_is_higher_or_equal_than_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('chocolate', 100.1)
        self.assertEqual("Product chocolate cost too much!", str(ve.exception))

    def test_correct_add_to_cart_adding_to_product_dict(self):
        result = self.shopping_cart.add_to_cart('chocolate', 10)
        self.assertEqual({'chocolate': 10}, self.shopping_cart.products)
        self.assertEqual(10, self.shopping_cart.products['chocolate'])
        self.assertEqual("chocolate product was successfully added to the cart!", result)

    def test_raise_value_error_removing_product_not_in_shopping_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('bread')
        self.assertEqual("No product with name bread in the cart!", str(ve.exception))

    def test_correct_item_remove_from_cart(self):
        self.shopping_cart.products['chocolate'] = 10
        result = self.shopping_cart.remove_from_cart('chocolate')
        self.assertEqual({}, self.shopping_cart.products)
        self.assertEqual("Product chocolate was successfully removed from the cart!", result)

    def test_correct_initialization_new_instance_with__add__(self):
        self.shopping_cart.products['chocolate'] = 10
        self.second_shopping_cart.products['bread'] = 20

        new_instance = self.shopping_cart.__add__(self.second_shopping_cart)

        self.assertEqual("MetroLIDL", new_instance.shop_name)
        self.assertEqual(150, new_instance.budget)
        self.assertEqual({'chocolate': 10, 'bread': 20}, new_instance.products)

    def test_raise_value_error_not_enough_money_to_buy_products(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.products['chocolate'] = 99
            self.shopping_cart.budget = 49
            self.shopping_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 50.00lv!", str(ve.exception))

    def test_correct_buy_products_func(self):
        self.shopping_cart.products['chocolate'] = 10
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 10.00lv.", result)


if __name__ == '__main__':
    main()
