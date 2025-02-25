# Property = Decorator used to define a method as a property (It can be accessed like attributes)
# Benefits = Add additional logic when read, write or delete attributes
# Give you setter, getter and deleter method
class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} CM"

    @property
    def height(self):
        return f"{self._height:.1f} CM"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero!")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero!")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted!")


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

# del rectangle.width
# del rectangle.height

print(rectangle.width)
print(rectangle.height)
print()


# Decorator = A function that extends behavior of another function.
# Add something to the base function without changing it
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("* You add sprinkles 🍭")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("* You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")


get_ice_cream(input("Enter your ice cream flavour: "))
print()

# Exception Handling = An event that interrupts the flow of a program
#             ZeroDivisionError (1 / 0), TypeError (1 + "1"), ValueError (int("pizza"))
#             1.try, 2.except, 3.finally
is_running = True

while is_running:
    try:
        number = int(input("Enter a number: "))
        print(round((1 / number), 3))
        is_running = False
    except ZeroDivisionError:
        print("You cannot divide by Zero!")
        continue
    except ValueError:
        print("Enter numbers only please!")
        continue
    except Exception:
        print("Something went wrong!")
        continue
    finally:
        print("Do some cleanup here!")
print()


# Python File Detection
import os

file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exist!")
    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("That is a directory.")
else:
    print("That location does not exist!")
print()

# Python writing files (.txt, .json, .csv)
# 'w' means write, 'x' if file already exist, 'a' for append

txt_file = "I love Kabob!"
file_path2 = "output.txt"

with open(file_path2, 'w') as file:
    file.write(txt_file)
    print(f"File {file_path2} was created!")

txt_file2 = "I Love Persian Food!"
file_path3 = "/Users/houmanirani/Desktop/Python_File.txt"

try:
    with open(file_path3, 'w') as file:
        file.write(txt_file2)
        print(f"File {file_path3} was created!")
except FileExistsError:
    print("File already exist!")

file_path4 = "/Users/houmanirani/Desktop/Python_File2.txt"
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

try:
    with open(file_path4, 'w') as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"File {file_path3} was created!")
except FileExistsError:
    print("File already exist!")

import json

employees2 = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

file_path4 = "/Users/houmanirani/Desktop/Python_File3.json"

try:
    with open(file_path4, 'w') as file:
        json.dump(employees2, file, indent=4)
        print(f"Json file {file_path4} was created!")
except FileExistsError:
    print("That file already exist!")

import csv

employees3 = [["Name", "Age", "Job"],
              ["Spongebob", 30, "Unemployed"],
              ["Patrick", 45, "Cook"],
              ["Sandy", 27, "Scientist"]]
file_path5 = "/Users/houmanirani/Desktop/Python_File3.csv"

try:
    with open(file_path5, 'w', newline="") as file:
        writer = csv.writer(file)
        for row in employees3:
            writer.writerow(row)
        print(f"CSV file {file_path5} was created!")
except FileExistsError:
    print("That file already exist!")
print()

# Python reading files (.txt, .json, .csv)
# For json instead of content = file.read() use content = json.load(file)
# For csv use content = csv.reader(file) and for loop instead. print first variable of the for loop.
# csv continued...   for line in content: print(line)

file_path5 = "/Users/houmanirani/Desktop/Python_File2.txt"

try:
    with open(file_path5, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File is not found!")
except PermissionError:
    print("You do not have permission to read that file!")