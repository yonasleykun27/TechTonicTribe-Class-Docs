# #Create a Person class and a Student class that inherits it. Add an id attribute to Student.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

# student = Student("Yonas", 22, "DBU1601770")
# print(f"Student name: {student.name}, Student age: {student.age}, Student id: {student.student_id}")

# #my implimentation

# class Person:
#     def __init__(self,name, age):
#         self.name= name
#         self.age=age
# class Student(Person):
#     def __init__(self, name, age, student_id ):
#         super(). __init__ (name,age)
#         self.student_id= student_id

# student=Student("yonas",20,"DBU1111")
# print(student.name, student.age, student.student_id)

# # Task 3: Create a Vehicle class with a method fuel_efficiency() and override it in Car and Bike subclasses.

# class Vehicle:
#     def fuel_efficiency(self):
#         return "General fuel efficiency"

# class Car(Vehicle):
#     def fuel_efficiency(self):
#         return "Car fuel efficiency: 15 km/l"

# class Bike(Vehicle):
#     def fuel_efficiency(self):
#         return "Bike fuel efficiency: 50 km/l"

# # Example usage
# car = Car()
# bike = Bike()
# print(car.fuel_efficiency())
# print(bike.fuel_efficiency())

# # Task 4: Implement a Shape class and a Square subclass that calculates the area.

# class Shape:
#     def __init__(self, length):
#         self.length = length

# class Square(Shape):
#     def area(self):
#         return self.length ** 2

# # Example usage
# square = Square(4)
# print("Area of square:", square.area())

# # Task 5: Use super() to call a parent class's method from a child class.

# class Parent:
#     def greet(self):
#         return "Hello from Parent"

# class Child(Parent):
#     def greet(self):
#         parent_greeting = super().greet()
#         return f"{parent_greeting}, and Hello from Child"

# # Example usage
# child = Child()
# print(child.greet())

# # Task 6: Create a Teacher class and inherit it in MathTeacher and ScienceTeacher.

# class Teacher:
#     def __init__(self, name):
#         self.name = name

# class MathTeacher(Teacher):
#     def teach(self):
#         return f"{self.name} teaches Mathematics"

# class ScienceTeacher(Teacher):
#     def teach(self):
#         return f"{self.name} teaches Science"

# # Example usage
# math_teacher = MathTeacher("Alice")
# science_teacher = ScienceTeacher("Bob")
# print(math_teacher.teach())
# print(science_teacher.teach())

# # Task 7: Demonstrate single inheritance using Company and Employee.

# class Company:
#     def __init__(self, name):
#         self.name = name

# class Employee(Company):
#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id

# # Example usage
# employee = Employee("TechCorp", "E123")
# print(employee.name, employee.employee_id)

# # Task 8: Write a program with a Device class and its subclasses Laptop and Smartphone, overriding the use method.


# class Device:
#     def use(self):
#         return "Using a device"

# class Laptop(Device):
#     def use(self):
#         return "Using a laptop for work"

# class Smartphone(Device):
#     def use(self):
#         return "Using a smartphone for communication"

# # Example usage
# laptop = Laptop()
# smartphone = Smartphone()
# print(laptop.use())
# print(smartphone.use())

# # Task 9: Create an example of multiple inheritance using Teacher and Mentor.


# class Teacher:
#     def teach(self):
#         return "Teaching students"

# class Mentor:
#     def guide(self):
#         return "Guiding students"

# class TeacherMentor(Teacher, Mentor):
#     pass

# # Example usage
# teacher_mentor = TeacherMentor()
# print(teacher_mentor.teach())
# print(teacher_mentor.guide())

# # Task 10: Write a program to demonstrate hierarchical inheritance with a Person class and subclasses.

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def study(self):
#         return f"{self.name} is studying"

# class Teacher(Person):
#     def teach(self):
#         return f"{self.name} is teaching"

# # Example usage
# student = Student("John")
# teacher = Teacher("Alice")
# print(student.study())
# print(teacher.teach())