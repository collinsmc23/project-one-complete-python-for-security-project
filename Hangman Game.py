import random

answerList = ['world', 'hello', 'this', 'is', 'me']

random.shuffle(answerList)

answer = list(answerList[0])


display = []

display.extend(answer)


for i in range(len(display)):
    display[i] = "_"

print(' '. join(display))
print()

count = 0

while count < len(answer):
    guess = input("Please guess a letter: ")
    guess = guess.lower()
    print(count)


    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            count = count + 1

    print(' '.join(display))
    print()

print("Well done, you guessed the word")





