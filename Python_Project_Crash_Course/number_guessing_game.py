import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it! Good luck!")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}:")
        
        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Yaaaay! Congrats! You guessed it in {attempt} tries!")
            break  
    
    if guess != random_number:
        print(f"\nGame Over!! The correct number was {random_number}. Better luck next time!")

number_guessing_game()