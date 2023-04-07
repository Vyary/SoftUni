from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_successful_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})

    def test_total_sold_books(self):
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_book_limit_setter_exception_with_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_book_limit_setter_exception_with_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -5

        self.assertEqual(str(ve.exception), "Books limit of -5 is not valid")

    def test_len_with_zero(self):
        self.assertEqual(len(self.bookstore), 0)

    def test_len_with_five_books(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Test1": 5,
            "Test2": 2,
            "Test3": 3,
            "Test4": 4,
            "Test5": 6,
        }

        self.assertEqual(len(self.bookstore), 20)

    def test_receive_book_exception_exceed_book_limit(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Test1", 15)

        self.assertEqual(
            str(ex.exception), "Books limit is reached. Cannot receive more books!"
        )

    def test_receive_book_success(self):
        result = self.bookstore.receive_book("Test4", 3)
        self.assertEqual(
            self.bookstore.availability_in_store_by_book_titles["Test4"], 3
        )
        self.assertEqual(result, "3 copies of Test4 are available in the bookstore.")

    def test_receive_book_if_already_available(self):
        self.bookstore.availability_in_store_by_book_titles = {"Test4": 3}
        result = self.bookstore.receive_book("Test4", 7)
        self.assertEqual(
            self.bookstore.availability_in_store_by_book_titles["Test4"], 10
        )
        self.assertEqual(result, "10 copies of Test4 are available in the bookstore.")

    def test_sell_book_exception_book_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Test1", 1)

        self.assertEqual(str(ex.exception), "Book Test1 doesn't exist!")
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_sell_book_exception_no_enough_quantity(self):
        self.bookstore.availability_in_store_by_book_titles = {"Test1": 8}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Test1", 10)

        self.assertEqual(
            str(ex.exception), "Test1 has not enough copies to sell. Left: 8"
        )
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_sell_book_success(self):
        self.bookstore.availability_in_store_by_book_titles = {"Test1": 8}
        result = self.bookstore.sell_book("Test1", 8)
        self.assertEqual(result, "Sold 8 copies of Test1")
        self.assertEqual(
            self.bookstore.availability_in_store_by_book_titles["Test1"], 0
        )
        self.assertEqual(len(self.bookstore), 0)
        self.assertEqual(self.bookstore.total_sold_books, 8)

        self.assertEqual(
            str(self.bookstore),
            "Total sold books: 8\nCurrent availability: 0\n - Test1: 0 copies",
        )


if __name__ == "__main__":
    main()
