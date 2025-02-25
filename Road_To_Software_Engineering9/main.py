# Dictionary = a collection of {key:value} pairs ordered and changeable. No duplicate keys
capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))
if capitals.get("Russia"):
    print("That Capital does exist")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"})
print(capitals.get("Germany"))
capitals.update({"USA": "New York"})
print(capitals)
capitals.pop("China")
print(capitals)
# capitals.popitem()         remove the last element
# capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
    print(key)

print()

values = capitals.values()
for value in capitals.values():
    print(value)

print()

items = capitals.items()
for key, value in capitals.items():
    print(f"{key:<8}: {value}")
print()

# Concession stand program
menu = {"pizza": 3.00, "nachos": 4.50, "popcorn": 6.00,
        "fries": 2.50, "chips": 1.00, "pretzel": 3.50, "soda": 3.00, "lemonade": 4.25}

cart = []
total = 0

print("---------- Menu ----------")
for key, value in menu.items():
    print(f"{key:<10}:  {value:.2f}")
print("-------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:  # It means that food exist
        cart.append(food)
    elif menu.get(food) is None:
        print("Your item does not exist!")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")
print()

# random numbers
import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(low, high)  # You can add value directly to, as well.
print(number)

number2 = random.random()
print(number2)

option = random.choice(options)
print(option)

random.shuffle(cards)
print(cards)





