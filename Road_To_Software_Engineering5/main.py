# Format Specifiers
price1 = 3000.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:10}")
print(f"Price 3 is ${price3:<10}")
print(f"Price 3 is ${price3:>10}")
print(f"Price 3 is ${price3:^10}")
print(f"Price 3 is ${price3:+}\n")


# While Loop, Very good for user input feedback
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}!\n")

age = int(input("Enter your age: "))

while age <= 0:
    print("Age cannot be zero or negative.")
    age = int(input("Enter your age: "))
print(f"Your age is {age}\n")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}!")
    food = input("Enter another food you like (q to quit): ")
print("Bye\n")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between 1 - 10: "))
print(f"You number is {num}.\n")

# Compound interest Calculator project
principle = 0
interest = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("Principle cannot be equal or less than zero!")

while interest <= 0:
    interest = float(input("Enter the interest: "))
    if interest <= 0:
        print("Interest cannot be equal or less than zero!")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time cannot be equal or less than zero!")

total = principle * pow((1 + interest / 100), time)
print(f"\nBalance after {time} year/s is ${total:.2f}")
