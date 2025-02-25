# Polymorphism  =  It means many forms. Polymorphism is more about iterating data.
# Two ways to achieve polymorphism
# 1- Inheritance          2- Duck typing

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm²")
print()


# Duck Typing  =   Object must have the minimum necessary attributes / methods.
# It's more about grouping together data and iteration

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:
    alive = False

    def speak(self):
        print("HONK!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
print()


# Static methods = A method that belong to a class rather than any object from the class (Instance Method)
# Usually used for general utility functions. No need to use self inside the method

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position


# Static methods
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Software Engineer"))

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# Instance methods
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print()


# Class Method = Allows operation related to class itself. Take (cls) instead of (self) as first parameter.
# No need of object when calling class methods

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of student: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.total_gpa == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())
print()


# Magic Methods  =  Dunder methods, __init__, __str__, __eq__
# They are automatically called by Python's built-in objects.
# They allow developers to customize the behavior of objects.

class Books:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Object equality
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # Object less than
    def __lt__(self, other):
        return self.pages < other.pages

    # Object greater than
    def __gt__(self, other):
        return self.pages > other.pages

    # Adding objects components
    def __add__(self, other):
        return f"{self.pages + other.pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "pages":
            return self.pages
        else:
            return f"Key {item} is not found!"


book1 = Books("The Hobbit", "J.R.R Tolkien", 310)
book2 = Books("Harry Potter", "J.K. Rowling", 223)
book3 = Books("The Lion, the Witch, the Wardrobe", "C.S. Lewis", 172)
book4 = Books("Harry Potter", "J.K. Rowling", 323)

print(book1)
print(book2)
print(book3)
print(book2 == book4)
print(book1 < book2)
print(book1 > book3)
print(book1 + book4)
print("Witch" in book3)
print(book1['author'])
print(book3['title'])
print(book4['pages'])
print(book4['audio'])