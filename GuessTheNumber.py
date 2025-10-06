# Guess the Number Game
import random as rnd

start, end = 1, 100
# This function generates a random number for the player to try and guess.
def generating_a_random_number(start, end):
    """ 
    This function is used to generate a random number between 1 and 100 (inclusive). 
    This is the number the player will try to guess.
    """

    print(f"Please wait, the program will generate a random number from {start} to {end} in a few seconds.\n")
    return rnd.randint(start, end)

# 

# This loop is used to input the player's guess and to check that everything is in order.
def player_attempts(generated_random_number, max_attempts = 10):
    """
    Function to let the player guess the number
    """
    # This variable is used to store the random number to prevent it from being lost in memory and to allow easy access.
    number_of_attempts = max_attempts
    while number_of_attempts:
        try:
            player_guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100.")
            continue
        # Checking whether the player's guess is correct or not.
        if not 1 <= player_guess <= 100:
            print("Number out of range! Please enter between 1 and 100.")
            continue

        if player_guess == generated_random_number:
            print(f"🎉 Congratulations! You guessed it right. The number was {generated_random_number}.\n")
            return True
        elif player_guess < generated_random_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        # After each attempt, the number of remaining attempts should decrease.
        number_of_attempts -= 1
        if number_of_attempts >= 3:
            print(f"Attempts remaining: {number_of_attempts}\n")
        elif number_of_attempts == 2: 
            print("You have two attempts remaining.\n")
        else:
            print("You have one attempt remaining.\n")

    if number_of_attempts == 0:
        print(f"Sorry, you’ve lost—the attempts are over. The number was {generated_random_number}.\n")

def main_game():
    print(  "Welcome to the number guessing game!\n\n" \
            "1- In this game, I will think of a number between 1 and 100, and you will try to guess it.\n" \
            "2- You have 10 attempts to guess the correct number.\n" \
            "3- Please try to enter a positive integer between 1 and 100.\n" \
            "4- I will give you hints about the number—whether it’s higher or lower than your guess.\n\n" \
            "Good luck!\n\n")
        
    while True:
        random_number = generating_a_random_number(start, end) 
        player_attempts(random_number)

        # Checking whether the player wants to play again or not. 
        play_again = input("Please, if you want to play again, press (y); if not, press (n): \n").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye 👋")
            break
        else: 
            random_number = generating_a_random_number(start, end) 
            player_attempts(random_number)

# Run the game
main_game()
