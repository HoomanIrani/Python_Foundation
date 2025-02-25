# Houman Irani
# This is my first Python program.
print("Hello World!\n")

# String
first_name = "Hooman"
food = "Pizza"
email = "Hooman@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}\n")

# Integer
age = 30
quantity = 7
num_of_students = 28

print(f"You are {age} years old")
print(f"You bought {quantity} of this item")
print(f"Your class has {num_of_students} students\n")

# Float
price = 10.99
gpa = 3.82
distance = 5.7

print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} miles\n")

# Boolean
is_student = True

if is_student:
    print("You are a student.\n")
else:
    print("You are not a student.\n")

# Type of Variable and Casting, very important when it comes to handling user input
print(type(first_name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

quantity = str(quantity)
print(quantity)
quantity += "2"
print(quantity)

# Useful to check if user has entered any input
last_name = ""
first_name = bool(first_name)
last_name = bool(last_name)
print(first_name)
print(last_name)

# User Input, Input is always a String. It needs to be converted if you need Integers, or Float
name = input("What is your name? ")
user_age = int(input("How old are you? "))
user_age += 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {user_age} years old\n")

# Rectangle project, Project 1
length = int(input("Enter the length of the rectangle? "))
width = int(input("Enter the width of the rectangle? "))

perimeter = (length + width) * 2
area = length * width

print(f"Perimeter of the rectangle is: {perimeter}")
print(f"Area of the rectangle is: {area}\n")

# Shopping cart, Project 2
item = input("Enter your item? ")
price = float(input("Enter the price of the item? "))
item_quantity = int(input("Enter the quantity? "))

total = price * item_quantity * 1.09  #tax
print(f"You have bought {item_quantity} X {item}/s")
print(f"Your total is ${round(total, 2)} with tax.\n")

# Madlib, Project 3
adjective1 = input("Enter an adjective (Description): ")
noun1 = input("Enter a noun (Person, Place, Thing): ")
adjective2 = input("Enter an adjective (Description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (Description): ")

print(f"Today I went in a {adjective1} zoo.")
print(f"In an exhibit I saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!\n")

# Arithmetic and Math
friend = 5
friend += 1
friend -= 1
friend *= 2
friend //= 2
friend **= 2
print(friend)

my_friends = 10
my_friends %= 3
print(my_friends)

# Build in Math functions
x = 3.14
y = -4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(y, 3)
# result = max(x, y, z)
result = min(x, y, z)
print(result)

import math

print(math.pi)
print(math.e)
print(math.ceil(x))
print(math.floor(x))
res = math.sqrt(x)
print(res)

# Calculate Circumference and area of circle, Project 4
# import math
radius = float(input("\nEnter the radius of a circle: "))
area = math.pi * pow(radius, 2)
circumference = (math.pi * radius * 2)
print(f"The circumference is: {round(circumference, 2)} cm")
print(f"The area of circle is: {round(area, 2)} cm^2")
