"""Student/member registration and display functions."""

from data import students


def add_student() -> None:
    print("\n---------- ADD STUDENT ----------")
    student_id = int(input("Enter Student ID: "))
    if any(student["id"] == student_id for student in students):
        print("Student ID already exists!")
        return
    students.append({"id": student_id, "name": input("Enter Student Name: "),
                     "course": input("Enter Course: ")})
    print("Student added successfully!")


def view_students() -> None:
    print("\n---------- ALL STUDENTS ----------")
    if not students:
        print("No students registered.")
        return
    for student in students:
        print(f"\nStudent ID : {student['id']}\nName       : {student['name']}\nCourse     : {student['course']}\n---------------------------")
