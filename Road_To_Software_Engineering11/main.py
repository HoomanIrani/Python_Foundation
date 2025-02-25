# Dice Roller Program
import random

dice_art = {

    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")}

dice = []
total = 0
num_of_dice = int(input("How many dice: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die

print()
print(f"Total: {total}\n")


# Functions  ==> A block of reusable code.
# Arguments: 1- Positional, 2- Default, 3- Keyword, 4- Arbitrary

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"Your are {age} years old!")
    print("Happy Birthday to you!")


happy_birthday("Hooman", 30)
print()


def display_invoice(user_name, amount, due_date):
    print(f"Hello {user_name}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("Hooman", 101.01, "01/02")
print()


def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(add(5, 7))
print(subtract(5, 7))
print(multiply(5, 7))
print(round(divide(5, 7), 3))
print()


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("hooman", "irani")
print(full_name)
print()


# Default Arguments
def net_price(list_price, discount=0, tax=0.1):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print(round(net_price(500, 0.1), 2))
print(net_price(500, 0.1, 0))
print()

# Make sure default arguments are after positional arguments.
import time

def count(end, start=0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done!")


count(7)
print()
count(26, 23)
print()


# Keyword Arguments
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1, area=310, first=560, last=4800)
print(phone_num)


# Arbitrary Argument
# *args     = allows you to pass multiple non-key arguments.
# **kwargs  = allows you to pass multiple keyword arguments.
# Need to use for loop most of the time to utilize *args and **kwargs

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 7, 2, 10, 24))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Aryan", "Irani")
print()
display_name("Hooman", "N", "Irani")
print()


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print()
print_address(street="10189 Viceroy Ct",
              apt="4",
              city="Cupertino",
              state="CA",
              zip="95014")


# Shipping label program
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(kwargs.get('street'))
        print(kwargs.get('pobox'))
    else:
        print(kwargs.get('street'))
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


print()
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="10189 Vicero Ct",
               apt=4,
               city="Cupertino",
               state="CA",
               zip="95014")
print()

# Iterables, all the Python collections are iterables. You cannot use reversed on Sets.
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")
print()

my_name = "Hooman Irani"

for character in my_name:
    print(character, end=" ")
print()

# Membership operator ==>  in, not in     Can be used in strings, lists, sets, tuples and dictionaries
word = "apple"
letter = input("\nGuess a letter in a secret word: ")

if letter in word:
    print(f"There is a {letter}\n")
else:
    print(f"{letter} was not found!\n")

grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}.\n")
else:
    print(f"{student} was not found!\n")

# Valid email project. (Do it on your own)
# Make sure email has both (@ and .) ask user for email and keep it going until you get a valid email.

is_running = True
email = input("Enter your email address: ")

while is_running:
    if '@' not in email:
        print("Your email address has to include '@', try again.")
        email = input("Enter your email address: ")
    elif '.' not in email:
        print("Your email address has to include '.', Try again.")
        email = input("Enter your email address: ")
    else:
        print("You're in!")
        is_running = False