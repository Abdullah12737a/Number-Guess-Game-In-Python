import random

secret_numbers = random.sample(range(1, 10), 5)
guesses_left = 10
guessed_numbers = []

print("Welome to number guessing game!\n")
print("Try to Guess number between 1 and 10, you have to guess 5 secret numbers, you have only 10 tries\n")
print("Good Luck!\n")


while guesses_left > 0 and len(guessed_numbers) <=5:
    guess = int(input("Enter your guess: "))
    if guess in secret_numbers and guess not in guessed_numbers:
        print("Congratulations you have guessed the right number!\n")
        guessed_numbers.append(guess)
    elif guess in guessed_numbers:
        print("You have already guessed this number!. Try again!\n")
    else:
        print("Incorrect Guess!. Try again!n\n")
        print(f"You have {guesses_left} guesses left")
        guesses_left -= 1

if len(guessed_numbers) == 5:
    print(f"Congratulations you have guessed all the number!\nThe secret numbers were{secret_numbers}.\n")
else:
    print(f"Try again!.\nThe secret numbers were{secret_numbers}.")
    
