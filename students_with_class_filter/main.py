from func import students, show_students, add_student, students_by_class


msg = """
Student Management System
1. Add Student
2. Show All Students
3. Show Students by Class
4. Exit
"""

while True:
    print(msg)
    choice = input("Enter your choice: ")

    if choice == '4':
        print("Exiting the program.")
        break

    if choice == '1':
        name = input("Enter student name: ")
        class_name = input("Enter class name: ")
        add_student(name, class_name)
        print("Student added successfully!\n")

    elif choice == '2':
        print("All Students:")
        show_students()
        print()

    elif choice == '3':
        class_name = input("Enter class name to filter: ")
        filtered_students = students_by_class(class_name)
        for student in filtered_students:
            print(f"Name: {student['name']}, Class: {student['class']}")

    else:
        print("Invalid choice. Please try again.\n")