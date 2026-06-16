import random

def play_game():
    print("\n--- Welcome to the Advanced Number Guessing Game ---")
    
    print("Choose your difficulty level:")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")
    
    
    while True:
        try:
            level = int(input("Enter 1, 2, or 3: "))
            if level == 1:
                max_num = 10
                break
            elif level == 2:
                max_num = 50
                break
            elif level == 3:
                max_num = 100
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number, not text.")

    
    right_number = random.randint(1, max_num)
    attempts = 0
    
    print(f"\nI've picked a secret number between 1 and {max_num}. Let's go!")

    while True:
        try:
            
            guessed_number = int(input("\nGuess a number: "))
            attempts += 1

            if guessed_number < 1 or guessed_number > max_num:
                print(f"Out of bounds! Keep your guess between 1 and {max_num}.")
            elif guessed_number > right_number:
                print("Too high! Give it another shot and choose a lower number.")
            elif guessed_number < right_number:
                print("Too low! Give it another shot and choose a higher number.")
            else:
                # Correct Guess
                print(f"\n🎉 Spot on! You guessed the number in {attempts} attempts.")
                break # Exit the game loop
                
        except ValueError:
            
            print("Invalid input! Please enter a valid whole number.")

def main():
    
    while True:
        play_game()
        
        # Ask to replay
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thank you for playing. See you next time! 👋")
            break


if __name__ == "__main__":
    main()