# List Comprehension
double = []

for i in range(1, 11):
    double.append(i * 2)

print(double)

# Alternatives
doubles = [i * 2 for i in range(1, 11)]
triples = [i * 3 for i in range(1, 11)]
print(doubles)
print(triples)

fruits = ["apple", "cherry", "banana", "peach", "orange"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)
print()

numbers = [1, -2, 3, -4, 5, -6, 7]
positive_num = [num for num in numbers if num > 0]
negative_num = [num for num in numbers if num < 0]
print(positive_num)
print(negative_num)
print()

grades = [59, 100, 78, 88, 93, 96, 84, 49, 67]
passing_grade = [grade for grade in grades if grade >= 70]
print(passing_grade)
print()


# Switch Statement or Match-Case statement
# Using switch statement is easier since we can just use case instead of if, elif, else

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday!"
        case 2:
            return "It is Monday!"
        case 3:
            return "It is Tuesday!"
        case 4:
            return "It is Wednesday!"
        case 5:
            return "It is Thursday!"
        case 6:
            return "It is Friday!"
        case 7:
            return "It is Saturday!"
        case _:
            return "Not a valid day!"


print(day_of_week(2))


def is_weekend(day):
    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case "sunday" | "saturday":
            return True
        case _:
            return False


print(is_weekend("sunday"))
print()

# Module:
# import math
# import math as m
# from math import pi

import example

result = example.pi
result1 = example.square(9)
result2 = example.cube(9)
result3 = example.circumference(10)
result4 = example.area(10)

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print()


# Variable Scoop = Where a variable is visible and accessible.
# Scope Resolution Priority = (LEGB) Local -> Enclosed -> Global -> Built-in


def greet(name):
    print(f"Hello, {name}!")


if __name__ == '__main__':
    print("This script is being run directly!")
    greet("Alice")

greet("Hooman")
