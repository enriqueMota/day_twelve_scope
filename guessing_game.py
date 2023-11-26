import random
from art import LOGO
answer = random.randint(1,100)
user_answer = 0
attempts = 0

print(LOGO)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty.lower() == 'easy':
    attempts = 8
elif difficulty.lower() == 'hard':
    attempts = 5
    
# print(f"Attempts: {attempts}")
# print(f"answer: {answer}")

def check_guess(input):
    if input == answer:
        print(f"You got it! The answer was {answer}.")
    elif input > answer:
        print("Too high.")
    elif input < answer:
        print("Too low.")


while attempts >= 0 and answer != user_answer:
    if attempts != 0:
        print("Guess again.")
    if attempts == 0:
        print("You lose.")
        exit()
    print(f"your have {attempts} attempts remaining to guess the number.")
    user_answer =  int(input("Make a guess: "))
    check_guess(user_answer)
    attempts -= 1