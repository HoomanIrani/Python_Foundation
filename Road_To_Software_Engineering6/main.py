# For Loop
for i in range(1, 11):
    print(i)
print("")

for i in reversed(range(1, 11)):
    print(i)
print("Happy new year!\n")

for i in range(1, 11, 3):
    print(i)
print("")

credit_number = "1234-5678-9012-3456"
for i in credit_number:
    print(i)
print("")

# important keywords for loops: break, continue. These two always come with if, elif, else
for i in range(1, 8):
    if i == 6:
        continue
    else:
        print(i)
print("")

for i in range(1, 8):
    if i == 5:
        break
    else:
        print(i)

# Countdown Timer program
import time

times = int(input("Enter a time in seconds: "))

for i in range(times, 0, -1):
    seconds = i % 60  # We use remainder because we don't want seconds and minutes exceed 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up!\n")

# Nested Loops
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()