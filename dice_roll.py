import random

count = 0
rolled_count = 0
print("----Dice Rolling Sim----")

print("This is a Dice Rolling Simulator")

user_input = input("Would you like to continue? (Enter y): ")



while user_input ==  'y':
    gen_random_num = random.randint(1,6)
    convert_to_str = str(gen_random_num)
    print("You rolled a " + convert_to_str)
    user_input = input("Would You like to Continue?: ")

    count += gen_random_num
    rolled_count += 1


print("Your rolls add up to ", count)
print("You rolled", rolled_count, "times.")



