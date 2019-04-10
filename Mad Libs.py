
person_in_room = input("Enter the name of this person: ")


count = 0
num = 1
listadjective = []

print("Enter in a total of 5 adjectives...")
while count < 5:
    print("Enter in adjective {} ".format(num))
    adjective = input(" ")
    listadjective.append(adjective)
    num = num + 1
    count = count + 1

count_noun = 0
num_noun = 1
listnoun = []

print("Enter in a total of 4 nouns")
while count_noun < 4:
    print("Enter in noun {}".format(num_noun))
    noun = input(" ")
    listnoun.append(noun)
    num_noun = num_noun + 1
    count_noun = count_noun + 1


print("Dear Art Teacher")

print("Please excuse", person_in_room, "for being late for your", listadjective[0], "art class.  It\'s my fault.  I feel")
print(listadjective[1], person_in_room, "was up until the ", listadjective[2], "hours of the morning finishing his/her", listadjective[3], "project")
print("Just as we were going out the", listadjective[4], "door, I saw that his/her only pair of", listnoun[0], "had a", listnoun[1])
print("in them.  He/she needed to change! Then it took me an hour to find my", listnoun[2], "to drive")
print("him/her to school that morning since,", person_in_room, "missed the", listnoun[3])



