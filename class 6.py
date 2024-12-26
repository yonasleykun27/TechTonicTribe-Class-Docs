#store person name age and list of fav color

# class Person:
#     def 
# __init__(self,name,age,favorite_color):
#         self.name=name
#         self.age=age
#         self.favorite_color=favorite_color
# Person1=Person("samuel",20,["red","white","blue"])

# print((Person1.favorite_color))

# #define a library class

# class Library :
#     def __init__(self, name, location,tittles):
#         self.name=name
#         self.location=location
#         self.tittles=tittles
# Lib1=Library("aberehot","4kilo",["Fiction","Educational","Story"])

# print(Lib1.tittles)

# #third

# class Student:
#     def __init__(self, name, age, grades, courses):
#         self.name = name
#         self.age = age
#         self.grades = grades
#         self.courses = courses

# student1 = Student("yonas", 22, {"Math": 50, "Programming": 85}, ["Math", "Programming", "History"])
# print(student1.grades)


# #question 4

# class Product:
#     def __init__(self, name, price, manufacturing_date):
#         self.name = name
#         self.price = price
#         self.manufacturing_date = manufacturing_date

# product = Product("Laptop", 1500, "2024-01-15")
# print(f"Product Name: {product.name}, Price: ${product.price}, Manufacturing Date: {product.manufacturing_date}")

# #question 1

# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year

#     def display_details(self):
#         print(f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}")

# # Example Usage
# book = Book("1984", "George Orwell", 1949)
# book.display_details()


#question2 

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f"Name: {self.name}, Species: {self.species}"

    @classmethod
    def display_class_info(cls):
        return "This class is used to represent animals with their name and species."

    @staticmethod
    def is_domestic(species):
        domestic_species = ["dog", "cat", "cow", "sheep"]
        return species.lower() in domestic_species

animal = Animal("Lion", "Wild")
print(animal.describe())
print(Animal.display_class_info())
print(Animal.is_domestic("dog"))

# @question 3

