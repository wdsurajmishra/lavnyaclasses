
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    

class Student(Person):  
    def __init__(self, name, age, course):
        super().__init__(name, age)  
        self.course = course

    def introduce(self):
        base_introduction = super().introduce()  
        return f"{base_introduction} I am studying {self.course}."
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} I teach {self.subject}."


    
# # Example usage:


# person = Person("Prince", 22)
# print(person.introduce())

student = Student("Prince", 22, "Python Programming")
print(student.introduce())

teacher = Teacher("Mr. Smith", 45, "Mathematics")
print(teacher.introduce())

print(student.name)


class New:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute


    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.__age} years old."    
    
    def get_age(self):
        return self.__age

new_person = New("Price", 30)

print(new_person.get_age())  # Accessing private attribute via getter method