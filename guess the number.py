from random import randint
from art import logo
def check(user_guess,correct_number):
    if user_guess == correct_number:
        return 0
    elif user_guess > correct_number:
        return "Too high"
    elif user_guess < correct_number:
        return "Too low"
HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10

def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_difficulty == 'easy':
        user_attempts = EASY_ATTEMPTS
    else:
        user_attempts = HARD_ATTEMPTS
    game_end = False
    CORRECT_NUMBER = randint(1,100)
    while not game_end:
        print(f"You have {user_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        result = check(user_guess,CORRECT_NUMBER)
        if result == 0:
            print("Congatulations! You guessed")
            game_end = True
        else:
            user_attempts-=1
            print(result)
        if user_attempts == 0:
            game_end = True
    if user_attempts == 0:
        print("You've run out of guesses, you lose.")

while input("Do you want to play 'Guess the number' game? Type 'y' for yes, 'n' for no. ")=='y':
    game()

