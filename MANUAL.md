# ShelfSmart User Manual

## Requirements

- Python 3.10 or newer
- A terminal or command prompt
- No extra Python packages

## Start the program

Open a terminal in the project folder and run:

```bash
python code.py
```

Enter the number beside the action you want. Follow the prompts to enter book or student details. Choose `14` to exit.

## Menu options

1. Add a book
2. View all books
3. Search by book ID
4. Search by book name
5. Issue a book to a registered student
6. Return a book
7. Remove an available book
8. Update book details
9. View available books
10. View issued books
11. View library statistics
12. Add a student member
13. View student members
14. Exit

## Suggested sample session

1. Select `12` and register a student with ID `101`.
2. Select `1` and add a book with ID `501`.
3. Select `5`, enter book ID `501`, and student ID `101` to issue it.
4. Select `10` to view issued books, or `11` to see current counts.
5. Select `6` and enter book ID `501` to return the book.

The screenshot in `screenshots/sample-output.png` shows an example session.

## Important behavior

- Book IDs and student IDs must be unique during a run.
- Only a registered student can borrow an available book.
- An issued book cannot be issued again or removed.
- The current program keeps data in memory. Books and students reset when the program exits.

## Files

- `code.py`: convenient program entry point.
- `main.py`: interactive menu.
- `book.py`: book operations.
- `member.py`: student member operations.
- `statement.py`: statistics output.
- `data.py`: shared in-memory records.

## Upload this project to GitHub

After creating an empty GitHub repository, open a terminal in this folder and run the following commands, replacing the URL with your repository URL:

```bash
git init
git add .
git commit -m "Add ShelfSmart library management system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/shelfsmart-library-management.git
git push -u origin main
```
