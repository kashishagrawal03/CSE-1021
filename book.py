"""Book operations for the library management system."""

from data import books, students


def _find_book(book_id: int) -> dict[str, object] | None:
    return next((book for book in books if book["id"] == book_id), None)


def add_book() -> None:
    print("\n---------- ADD BOOK ----------")
    book_id = int(input("Enter Book ID: "))
    if _find_book(book_id):
        print("Book ID already exists!")
        return
    books.append({"id": book_id, "name": input("Enter Book Name: "),
                  "author": input("Enter Author Name: "), "status": "Available",
                  "issued_to": "None"})
    print("Book added successfully!")


def view_books() -> None:
    print("\n---------- ALL BOOKS ----------")
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"\nBook ID     : {book['id']}\nBook Name   : {book['name']}\nAuthor      : {book['author']}\nStatus      : {book['status']}\nIssued To   : {book['issued_to']}\n-------------------------------")


def search_by_id() -> None:
    print("\n---------- SEARCH BOOK ----------")
    book = _find_book(int(input("Enter Book ID: ")))
    if book:
        print(f"\nBook Found!\nBook ID   : {book['id']}\nName      : {book['name']}\nAuthor    : {book['author']}\nStatus    : {book['status']}\nIssued To : {book['issued_to']}")
    else:
        print("Book not found.")


def search_by_name() -> None:
    print("\n---------- SEARCH BOOK ----------")
    name = input("Enter Book Name: ").casefold()
    matches = [book for book in books if str(book["name"]).casefold() == name]
    if not matches:
        print("Book not found.")
        return
    for book in matches:
        print(f"\nBook Found!\nBook ID   : {book['id']}\nName      : {book['name']}\nAuthor    : {book['author']}\nStatus    : {book['status']}")


def issue_book() -> None:
    print("\n---------- ISSUE BOOK ----------")
    book = _find_book(int(input("Enter Book ID: ")))
    if not book:
        print("Book not found.")
        return
    if book["status"] == "Issued":
        print("Book is already issued.")
        return
    student_id = int(input("Enter Student ID: "))
    student = next((item for item in students if item["id"] == student_id), None)
    if not student:
        print("Student not found.")
        return
    book["status"] = "Issued"
    book["issued_to"] = student["name"]
    print("Book issued successfully!")


def return_book() -> None:
    print("\n---------- RETURN BOOK ----------")
    book = _find_book(int(input("Enter Book ID: ")))
    if not book:
        print("Book not found.")
    elif book["status"] == "Available":
        print("This book is not issued.")
    else:
        book["status"] = "Available"
        book["issued_to"] = "None"
        print("Book returned successfully!")


def remove_book() -> None:
    print("\n---------- REMOVE BOOK ----------")
    book = _find_book(int(input("Enter Book ID: ")))
    if not book:
        print("Book not found.")
    elif book["status"] == "Issued":
        print("Issued books cannot be removed.")
    else:
        books.remove(book)
        print("Book removed successfully!")


def update_book() -> None:
    print("\n---------- UPDATE BOOK ----------")
    book = _find_book(int(input("Enter Book ID: ")))
    if not book:
        print("Book not found.")
        return
    print("Current Name  :", book["name"])
    print("Current Author:", book["author"])
    book["name"] = input("Enter New Book Name: ")
    book["author"] = input("Enter New Author Name: ")
    print("Book details updated!")


def available_books() -> None:
    print("\n---------- AVAILABLE BOOKS ----------")
    found = [book for book in books if book["status"] == "Available"]
    if not found:
        print("No books are currently available.")
        return
    for book in found:
        print(f"ID: {book['id']} | Name: {book['name']} | Author: {book['author']}")


def issued_books() -> None:
    print("\n---------- ISSUED BOOKS ----------")
    found = [book for book in books if book["status"] == "Issued"]
    if not found:
        print("No books are currently issued.")
        return
    for book in found:
        print(f"ID: {book['id']}\nName: {book['name']}\nAuthor: {book['author']}\nIssued To: {book['issued_to']}\n-------------------------")
