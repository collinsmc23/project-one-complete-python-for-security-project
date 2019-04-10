import random


def prompt():
    gen_random_number = random.randint(1,15)
    user_guess = int(input("Guess the right number: "))
    if user_guess == gen_random_number:
        print("You got it!")
    else:
        while user_guess != gen_random_number:
                print("Try again")
                if user_guess > gen_random_number:
                    print("Guess Lower")
                elif user_guess < gen_random_number:
                    print("Guess Higher")
                user_guess = int(input("Guess the right number:  "))
                if user_guess == gen_random_number:
                    print("You got it!")




prompt()

