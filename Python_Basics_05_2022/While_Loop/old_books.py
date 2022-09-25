book_to_look_for = input()
current_book = input()
books_checked = 0
no_more_books = False

while current_book != book_to_look_for:
    if current_book == 'No More Books':
        no_more_books = True
        break
    books_checked += 1
    current_book = input()

if no_more_books:
    print(f"The book you search is not here!")
    print(f"You checked {books_checked} books.")
else:
    print(f"You checked {books_checked} books and found it.")
