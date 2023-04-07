import sys

sys.path.append(
    "e:\\Things\\Code\\SoftUni\\python-OOP-course\\exams\\22-august-2022\\unit_testing"
)
from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("TestShop", 100)

    def test_proper_initialization(self):
        self.assertEqual(self.shopping_cart.shop_name, "TestShop")
        self.assertEqual(self.shopping_cart.budget, 100)
        self.assertEqual(self.shopping_cart.products, {})

    def test_shop_name_exception_start_with_capital_letter(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("testshop", 1000)
        self.assertEqual(
            str(ex.exception),
            "Shop must contain only letters and must start with capital letter!",
        )

    def test_shop_name_exception_contain_only_letter(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("test1", 1000)
        self.assertEqual(
            str(ex.exception),
            "Shop must contain only letters and must start with capital letter!",
        )

    def test_add_to_cart_exception_cost_too_much(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart("testy", 101)
        self.assertEqual(str(ex.exception), "Product testy cost too much!")

    def test_add_to_cart_success(self):
        message = self.shopping_cart.add_to_cart("testy", 80)
        self.assertEqual(self.shopping_cart.products["testy"], 80)
        self.assertEqual(message, "testy product was successfully added to the cart!")
        self.shopping_cart.add_to_cart("testy", 75)
        self.assertEqual(self.shopping_cart.products["testy"], 75)

    def test_remove_from_cart_exception_no_product_with_this_name(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.remove_from_cart("testy")
        self.assertEqual(str(ex.exception), "No product with name testy in the cart!")

    def test_remove_from_cart_success(self):
        self.shopping_cart.add_to_cart("testy", 80)
        message = self.shopping_cart.remove_from_cart("testy")
        self.assertEqual(self.shopping_cart.products, {})
        self.assertEqual(
            message, "Product testy was successfully removed from the cart!"
        )
        self.shopping_cart.add_to_cart("testy", 80)
        self.shopping_cart.add_to_cart("testy2", 20)
        self.shopping_cart.remove_from_cart("testy")
        self.assertEqual(self.shopping_cart.products, {"testy2": 20})

    def test_add_carts_together(self):
        self.shopping_cart.add_to_cart("testy", 80)
        self.shopping_cart2 = ShoppingCart("Tet", 100)
        self.shopping_cart2.add_to_cart("testy", 80)
        self.shopping_cart2.add_to_cart("cheesy", 20)
        self.combined_cart = self.shopping_cart + self.shopping_cart2
        self.assertEqual(self.combined_cart.shop_name, "TestShopTet")
        self.assertEqual(self.combined_cart.budget, 200)
        self.assertEqual(self.combined_cart.products, {"testy": 80, "cheesy": 20})

    def test_buy_products_exception_not_enough_money(self):
        self.shopping_cart.add_to_cart("testy", 80)
        self.shopping_cart.add_to_cart("glass", 30)
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.buy_products()
        self.assertEqual(
            str(ex.exception),
            "Not enough money to buy the products! Over budget with 10.00lv!",
        )

    def test_buy_products_success(self):
        self.shopping_cart.add_to_cart("testy", 80)
        message = self.shopping_cart.buy_products()
        self.assertEqual(
            message, "Products were successfully bought! Total cost: 80.00lv."
        )


if __name__ == "__main__":
    main()
