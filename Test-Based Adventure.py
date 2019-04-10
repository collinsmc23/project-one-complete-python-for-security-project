print("---Test Based Adventure Game---")


print("Mission:  Find the I.T. Nerd, good luck!")

print("----------------------------------")
print("You walk into the dormitory and see two objects that stand out to you:  a window & a door")
decision1 = input("What do you do? [Enter 1 for Window or 2 for Door]:  ")

option1 = "1"
option2 = "2"
can = False

def door_opened():
    print()
    print("You see the door dresser is slightly opened, you walk towards it")

if decision1 == option1:
    print("You go up to the Window and see it's locked in place")
    print()
    print("You can try to unlock the door or walk back from where you came from")
    print()
    decision1_1 = input("What do you do? [Enter 1 for Unlocking the Window or 2 for Walking Back]:  ")
    if decision1_1 == option1:
        print("You see the Window is locked in place and can't be broken, you look back")
        door_opened()
    if decision1_1 == option2:
        door_opened()
if decision1 == option2:
    print("You go up to the door and it's open slightly.")
    print()
    print("You see a can of deodorant, do you pick this can up or leave?")
    print()
    decsion11_2 = input("What do you do? [Enter 1 to Pick up Can or 2 for leaving the can behind]:  ")
    if decsion11_2 == option1:
        print("You pick up the can and look back towards the desser door...")
        can = True
        door_opened()
    if decsion11_2 == option2:
        door_opened()


print()
print("You open the door and find the I.T. Nerd smells of Body Odor...")


if can == True:
    print()
    print("---Mission complete---")
    print()
    print("Good job I.T. Nerd Hunter, you give him the can of deodorant... and found him")


if can == False:
    print()
    print("---Mission Half-Completed---")
    print()
    print("You found the I.T. Nerd, but didn't get the deodorant..., mission half completed...")
