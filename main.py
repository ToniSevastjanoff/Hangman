# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']
guessed_chars = set()
random.seed()
answer = words[random.randrange(0, 4)]
lives = 8
ready = False
selection = ""

while selection != "play" and selection != "exit":
    print("H A N G M A N")
    print("Type 'play' to play the game, 'exit' to quit:")
    selection = input()
    print("")
    if selection == "exit":
        exit()

while lives > 0 and ready == False:
    # print("Lives:", lives)
    ready = True

    print("")

    for y in range(0, len(answer)):  # tulostetaan vihje
        if answer[y] in guessed_chars:
            print(answer[y], end="")
        else:
            print("-", end="")

    print("")
    letter = str((input("Input a letter: ")))  # syötetään arvaus

    if len(letter) > 1:  # tarkistetaan syötetyn tekstin pituus
        print("You should input a single letter")
        ready = False
        continue

    if not "a" <= letter <= "z":  # tarkistetaan että on annettu kirjain
        print("Please enter a lowercase English letter")
        ready = False
        continue

    if letter in answer:  # jos kirjain on vastauksessa

        if letter in guessed_chars:  # jos kirjain on jo arvattu
            print("You've already guessed this letter")
            # continue
        else:
            guessed_chars.add(letter)  # lisätään arvattu kirjain listaan
            # continue

    else:  # jos kirjain ei ole vastauksessa

        if letter in guessed_chars:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
            guessed_chars.add(letter)

    ready = True
    for y in range(0, len(answer)):  # tarkistetaan onko kaikki kirjaimet arvattu
        if answer[y] not in guessed_chars:
            ready = False
            continue

if ready:
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")