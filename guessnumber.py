import random

def guess_the_number():
    # Randomly choose a number between 1 and 100
    secret_number = random.randint(1, 100)

    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it!")
            break

# Run the game
guess_the_number()
