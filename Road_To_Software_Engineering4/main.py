# Logical Operator

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.\n")
else:
    print("The outdoor event is scheduled.\n")

temp2 = 45
is_sunny = True

if temp2 > 28 and is_sunny:
    print("It's Hot outside!")
    print("It's Sunny!\n")
elif temp2 <= 0 and is_sunny:
    print("It's Cold outside!")
    print("It's Sunny!\n")
elif 0 < temp2 < 28 and is_sunny:
    print("It's Warm outside!")
    print("It's Sunny!\n")
elif temp2 > 28 and not is_sunny:
    print("It's Hot outside!")
    print("It's Cloudy!\n")
elif temp2 <= 0 and not is_sunny:
    print("It's Cold outside!")
    print("It's Cloudy!\n")
elif 0 < temp2 < 28 and not is_sunny:
    print("It's Warm outside!")
    print("It's Cloudy!\n")

# Conditional Expression
num = 5
print("Positive" if num > 0 else "Negative")

num2 = 6
print("Even\n" if num2 % 2 == 0 else "Odd\n")

a = 6
b = 7
bigger = a if a > b else b
print(bigger)


# String Methods
name = input("\nWhat is your name: ")
phone_number = input("What is your phone number: ")
length = len(name)
result = name.find("n")
result2 = name.rfind("o")
result3 = name.capitalize()
result4 = name.upper()
result5 = name.lower()
result6 = name.isdigit()
result7 = name.isalpha()
result8 = phone_number.count("-")
phone_number = phone_number.replace("-", " ")
print(length)
print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(phone_number)

# print(help(str))

# Validate user input
username = input("\nEnter your username: ")
if len(username) > 12:
    print("Username is too long!\n")
elif username.find(" ") != -1:
    print("Username cannot include any spaces!\n")
elif not username.isalpha():
    print("Username cannot include any digits!\n")
else:
    print(f"Welcome {username}\n")


# String Indexing
credit_number = "1234-5678-9012-3477"
print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
credit_number = credit_number[::-1]
print(credit_number)
