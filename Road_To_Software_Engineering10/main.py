# Number Guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("Python number guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, try again!")
        elif guess > answer:
            print("Too high! try again!")
        else:
            print(f"Correct! The answer was {answer}.")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Guess!")
        print(f"Please select a number between {lowest_num} and {highest_num}")
print()

# Rock, paper, scissors game
import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n) ").lower()
    if play_again == "y":
        pass
    else:
        running = False

print()
print("Thanks for playing!")
