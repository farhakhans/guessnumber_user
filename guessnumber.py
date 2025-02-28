import random

def guess_the_number():
    print("🎮 Welcome to the Number Guessing Game!")
    print("Select Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    
    while True:
        try:
            choice = int(input("Enter difficulty level (1/2/3): "))
            if choice == 1:
                max_number = 50
                break
            elif choice == 2:
                max_number = 100
                break
            elif choice == 3:
                max_number = 200
                break
            else:
                print("❌ Invalid choice! Please select 1, 2, or 3.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    # Generate random number
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {max_number}. Can you guess it?")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("🔼 Too low! Try again.")
            elif user_guess > secret_number:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the right number: {secret_number}")
                print(f"🏆 Total Attempts: {attempts}")
                break  # Game ends
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Run the game
guess_the_number()
