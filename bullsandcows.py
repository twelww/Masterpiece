import random

# Generate a random four-digit number with no repeating digits
number = ''.join(random.sample('0123456789', 4))

# Define the initial number of attempts
attempts = 0

# Allow the user to guess the number
while True:
    guess = input("Guess a four-digit number with no repeating digits: ")
    attempts += 1
    
    # Check if the guess is valid
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
        print("Invalid guess. Please enter a four-digit number with no repeating digits.")
        continue
    
    # Check if the guess is correct
    bulls = sum(1 for i in range(4) if guess[i] == number[i])
    cows = sum(1 for i in range(4) if guess[i] in number and guess[i] != number[i])
    print("Bulls:", bulls, "Cows:", cows)
    
    if bulls == 4:
        print("Congratulations, you guessed the number in", attempts, "attempts!")
        break
