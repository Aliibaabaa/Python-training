import random

# Generate a random number between 1 and 100
secretNumber = random.randint(1, 100)
attempts = 5

print("======================================================================")
print("- - - -                 GUESS-THE-NUMBER GAME                 - - - -")
print("======================================================================")
print("** Try to guess a number between 1 and 100. You have 5 attempts. **")
print("----------------------------------------------------------------------")

while attempts > 0:
    try:
        userGuess = int(input("Enter your guess: "))

        if 1 <= userGuess <= 100:
            if userGuess == secretNumber:
                print("======================================================================")
                print("Congratulations! You guessed the number right!")
                print("======================================================================")
                break
            elif userGuess > secretNumber:
                attempts -= 1
                print(f"That's too high. Try again! You have {attempts} attempts remaining.\n")
            else:
                attempts -= 1
                print(f"That's too low. Try again! You have {attempts} attempts remaining.\n")
        else:
            print("Invalid input. Please enter a number between 1 and 100.\n")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.\n")

if attempts == 0:
    print("======================================================================")
    print(f"Sorry! You've run out of attempts. The secret number was {secretNumber}. \nThank you for playing!")
    print("======================================================================")
