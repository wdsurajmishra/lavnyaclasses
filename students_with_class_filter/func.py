students = []

def add_student(name, class_name):
    student = {
        'name': name,
        'class': class_name
    }
    students.append(student)


def show_students():
    for student in students:
        print(f"Name: {student['name']}, Class: {student['class']}")
        
        
def students_by_class(class_name):
    filter_students = []
    for student in students:
        if student['class'] == class_name:
            filter_students.append(student)

    return filter_students


