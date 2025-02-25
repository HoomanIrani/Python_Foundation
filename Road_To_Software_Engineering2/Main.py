# if statement, How you put them in order is extremely important
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You have not been born! lol")
else:
    print("You must be 18+ to sign up!")


# Practice 1
response = input("Would you like food? (Y/N): ").upper()
if response == "Y":
    print("Have some food.")
else:
    print("No food for you.")


# Practice 2
name = input("Enter your name: ")
if name == "":
    print("You did not type your name!")
else:
    print(f"Hello {name}")

# Practice 3
online = True
if online:
    print("You are Online!\n")
else:
    print("You are Offline!\n")

# Simple Calculator project
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator.")