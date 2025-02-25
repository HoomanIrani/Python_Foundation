# Weight converter program
weight = float(input("Enter your weight: "))
unit = input("Enter the unit (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid!")
print()


# Temperature converter program
temp_unit = input("Is this temperature in Celsius or Fahrenheit (C / F): ").upper()
temp = float(input("Enter the temperature: "))

if temp_unit == "C":
    temp = temp * 9 / 5 + 32
    temp_unit = "Fahrenheit."
    print(f"Temperature is {round(temp)} {temp_unit}")
elif temp_unit == "F":
    temp = (temp - 32) * 5 / 9
    temp_unit = "Celsius."
    print(f"Temperature is {round(temp)} {temp_unit}")
else:
    print(f"{temp_unit} is not valid!")