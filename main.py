"""Run the command-line library management system."""

from book import (add_book, available_books, issue_book, issued_books,
                  remove_book, return_book, search_by_id, search_by_name,
                  update_book, view_books)
from member import add_student, view_students
from statement import statistics


def main() -> None:
    actions = {
        "1": add_book, "2": view_books, "3": search_by_id,
        "4": search_by_name, "5": issue_book, "6": return_book,
        "7": remove_book, "8": update_book, "9": available_books,
        "10": issued_books, "11": statistics, "12": add_student,
        "13": view_students,
    }
    while True:
        print("\n========================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Book\n2. View All Books\n3. Search Book by ID\n4. Search Book by Name")
        print("5. Issue Book\n6. Return Book\n7. Remove Book\n8. Update Book")
        print("9. Show Available Books\n10. Show Issued Books\n11. Library Statistics")
        print("12. Add Student\n13. View Students\n14. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "14":
            print("\nThank you for using the Library Management System!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
