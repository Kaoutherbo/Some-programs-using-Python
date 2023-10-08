import random

lower_limit = 1
upper_limit = 100
secret_number = random.randint(lower_limit, upper_limit)

print(f"Guess the number between {lower_limit} and {upper_limit}!")

while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Try a higher number.")
    elif guess > secret_number:
        print("Try a lower number.")
    else:
        print(f"Congratulations! You guessed the secret number, {secret_number}!")
        break
