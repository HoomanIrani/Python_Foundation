# Collection is a single variable used to store multiple values.
# List = Ordered and changeable. Duplicates Ok.
# Set = Unordered and immutable, but add / remove ok. No Duplicates
# Tuple = Ordered and unchangeable. Duplicates ok. Faster

# List
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))

print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"
print(fruits)
fruits.append("cherry")
print(fruits)
fruits.remove("pineapple")
fruits.insert(0, "pear")
print(fruits)
fruits.sort()
fruits.reverse()
print(fruits)

# fruit.clear()
print(fruits.index("cherry"))
print(fruits.count("pear"))
print()

# Set
stocks = {"tesla", "apple", "google", "nvidia"}
print(len(stocks))
print("tesla" in stocks)
stocks.add("amazon")
stocks.remove("tesla")
stocks.pop()
print(stocks)
# stocks.discard()   Similar to remove, but even if element does not exist it does not create an error.
# stocks.clear()

for stock in stocks:
    print(stock)
print()

# Tuples
foods = ("burger", "pizza", "pasta")
print(len(foods))
print("pizza" in foods)
print(foods.index("pasta"))
print(foods.count("burger"))

for food in foods:
    print(food)
print()

# Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Enter your food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for food in foods:
    print(food, end="  ")

print()

for price in prices:
    total += price

print(f"Your total will be ${round(total, 2)}")
print()

# 2D Collection
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"],
# ["chicken", "fish", "turkey"]]

print(groceries)
print(groceries[2][1])

for collection in groceries:
    print(collection)

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

print()

# Phone pad exercise
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for nums in num_pad:
    for num in nums:
        print(num, end="  ")
    print()