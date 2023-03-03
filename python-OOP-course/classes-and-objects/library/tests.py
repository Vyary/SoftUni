from project.library import Library
from project.user import User
from project.registration import Registration


user1 = User(123, "Morgan")
print(user1)
library1 = Library()
library1.books_available.update(
    {
        "J.K.Rowling": [
            "The Chamber of Secrets",
            "The Prisoner of Azkaban",
            "The Goblet of Fire",
            "The Order of the Phoenix",
            "The Half-Blood Prince",
            "The Deathly Hallows",
        ]
    }
)
register = Registration()
register.add_user(user1, library1)
print(library1.get_book("J.K.Rowling", "The Goblet of Fire", 10, user1))
print(user1)
print(library1.rented_books)
register.change_username(123, "John", library1)
print(library1.rented_books)
print(library1.books_available)
