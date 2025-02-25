# Object-Oriented Programming
# Object = A bundle of related attributes and methods
# Class = (Blueprint) Used to design the structure and layout of an object

from car import Car
from student import Student

car1 = Car("Lexus", 2020, "Silver", False)
car2 = Car("Ferrari", 2024, "Red", True)

print(car1.year, car1.color, car1.model, car1.for_sale)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car2.stop()
car2.describe()

print()

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(Student.class_year)
print(Student.num_student)
print(f"\nMy graduating class of {student1.class_year} has {student2.num_student} students.")
print()

# Inheritance = Allows a class to inherit attributes and methods from another class.
# Helps with code usability and extensibility.

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleeping(self):
        print(f"{self.name} is sleeping!")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Mouse(Animal):
    pass


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleeping()
print()

# Multiple Inheritance   =>  Inherit from more than one parents.
# Multilevel Inheritance =>  Inherit from a parent which inherit from another parent.

class Prey(Animal):
    def flee(self):
        print("Animal is fleeing!")


class Predator(Animal):
    def hunt(self):
        print("This Animal is Hunting!")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bunny")
hawk = Hawk("Hooman")
fish = Fish("Googooli")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
fish.eat()
rabbit.sleeping()
print()


# Super()  =  Function used in a child class to call methods from a parent class
# Allows you to extend functionality of the inherited method.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")  # Very Useful


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height}")
        super().describe()


circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=6)
triangle = Triangle(color="yellow", filled=True, width=7, height=8)

print(circle.color)
print(circle.filled)
print(circle.radius)
print(square.color, square.filled, square.width)
print(triangle.color, triangle.filled, triangle.width, triangle.height)
circle.describe()
square.describe()
triangle.describe()