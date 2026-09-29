"""Library summary and statistics."""

from data import books, students


def statistics() -> None:
    available = sum(book["status"] == "Available" for book in books)
    issued = sum(book["status"] == "Issued" for book in books)
    print("\n---------- LIBRARY STATISTICS ----------")
    print("Total Books     :", len(books))
    print("Available Books :", available)
    print("Issued Books    :", issued)
    print("Total Students  :", len(students))
