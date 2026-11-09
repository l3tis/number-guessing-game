import random

number = random.randint(1, 100)
attempts = 7

print("I'm thinking of a number between 1 and 100. You have 7 tries!")

while attempts > 0:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a number.")
        continue

    attempts -= 1

    if guess == number:
        print("Congratulations, you got it! 🎉")
        break
    elif guess < number:
        print(f"Higher. Attempts left: {attempts}")
    else:
        print(f"Lower. Attempts left: {attempts}")
else:
    print(f"Out of tries. The number was {number}.")
