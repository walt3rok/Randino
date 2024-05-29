import random

def get_valid_guess():
    while True:
        guess = input("Enter your guess (or type 'quit' to exit): ")
        
        if guess.strip().lower() == "quit":
            print("Exiting the game. Goodbye!")
            exit()  # Exit the game if the user enters "quit"
        
        if guess.strip() == "":
            print("Please enter a valid number.")
        else:
            try:
                guess = int(guess)
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    while True:
        guess = get_valid_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing a higher number.")
        elif guess > secret_number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

# Call the function to start the game
number_guessing_game()
