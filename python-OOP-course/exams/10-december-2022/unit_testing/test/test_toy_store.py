import unittest
from project.toy_store import ToyStore

class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_add_toy_success(self):
        result = self.toy_store.add_toy("A", "Car")
        self.assertEqual(result, "Toy:Car placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf["A"], "Car")

    def test_add_toy_failure_shelf_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("H", "Car")
        self.assertTrue("Shelf doesn't exist!" in str(context.exception))

    def test_add_toy_failure_shelf_already_taken(self):
        self.toy_store.toy_shelf["A"] = "Car"
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("A", "Train")
        self.assertTrue("Shelf is already taken!" in str(context.exception))

    def test_add_toy_failure_toy_already_in_shelf(self):
        self.toy_store.toy_shelf["A"] = "Car"
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("A", "Car")
        self.assertTrue("Toy is already in shelf!" in str(context.exception))

    def test_remove_toy_success(self):
        self.toy_store.toy_shelf["A"] = "Car"
        result = self.toy_store.remove_toy("A", "Car")
        self.assertEqual(result, "Remove toy:Car successfully!")
        self.assertIsNone(self.toy_store.toy_shelf["A"])

    def test_remove_toy_failure_shelf_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy("H", "Car")
        self.assertTrue("Shelf doesn't exist!" in str(context.exception))

    def test_remove_toy_failure_toy_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy("A", "Car")
        self.assertTrue("Toy in that shelf doesn't exists!" in str(context.exception))

    def test_init_toy_shelf_keys(self):
        self.assertEqual(list(self.toy_store.toy_shelf.keys()), ["A", "B", "C", "D", "E", "F", "G"])

    def test_init_toy_shelf_values(self):
        self.assertEqual(list(self.toy_store.toy_shelf.values()), [None, None, None, None, None, None, None])

if __name__ == '__main__':
    unittest.main()