import pandas as pd
import random
import sys
import time

alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guessed_letters = []
file1 = pd.read_csv("word_list.csv")
word_list = file1.values.flatten().tolist()
word1 = random.choice(word_list)
lives = 8
print("\033[35m" + f"word consists of {len(word1)} letters" + "\033[0m")

while True:
    a = input("guess a letter(l) or guess the word(w): ").lower()
    if lives >= 4:
        print("\033[34m" + f"Lives left: {lives}" + "\033[0m")
    else:
        print("\033[31m" + f"Lives left: {lives}" + "\033[0m")
    if len(guessed_letters) != 0:
        print("\033[36m"+"Guessed letters: " + "\033[0m", end="")
        count2 = 0
        for i in guessed_letters:
            count2 += 1
            if count2 == len(guessed_letters):
                print("\033[36m" + i + "\033[0m")
            else:
                print("\033[36m" + i, end=", ")
    else:
        pass
    if a == "l":
        b = input("Your guess: ")
        if b in alphabet1:
            if b not in guessed_letters:
                if b in word1:
                    guessed_letters += b
                    count1 = 0
                    for i in word1:
                        if i == b:
                            count1 += 1
                        else:
                            pass
                    if count1 > 1:
                        print("\033[94;1m" + f"{b} is in word {count1} times!" + "\033[0m", end = "")
                        time.sleep(1)
                    else:
                        print("\033[94;1m" + f"{b} is in word {count1} time!" + "\033[0m", end="")
                        time.sleep(1)
                    print("\n")
                    print("\033[33m" + "Word: " + "\033[0m", end="")
                    for i in word1:
                        if i in guessed_letters:
                            print("\033[97;1m" + i + "\033[0m", end="")
                        else:
                            print("\033[97;1m" + "_" + "\033[0m", end="")
                    print("\n")
                else:
                    print("\033[31m" + "Wrong guess" + "\033[0m", end="")
                    time.sleep(1)
                    print("\n")
                    print("\033[33m" + "Word: " + "\033[0m", end="")
                    for i in word1:
                        if i in guessed_letters:
                            print("\033[97;1m" + i + "\033[0m", end="")
                        else:
                            print("\033[97;1m" + "_" + "\033[0m", end="")
                    print("\n")
                    lives -= 1
                    guessed_letters += b
            else:
                print("\033[36m" + f"You already guessed {b}" + "\033[0m")
                time.sleep(1)
        else:
            print("Invalid letter")
    elif a == "w":
        c = input("Your guess: ").strip().lower()
        if c == word1:
            print("\033[92;1m" + "Correct guess!" + "\033[0m")
            time.sleep(1)
            print("\n" + "\033[34m" + "You Win!" + "\033[0m")
            sys.exit("")
        else:
            print("\033[31m" + "Wrong guess!" + "\033[0m")
            time.sleep(1)
            print("\033[34m" + f"Word was {word1}" + "\n" + "\033[0m")
            time.sleep(1)
            sys.exit("You lose!")
    else:
        print("\033[31m" + "Wrong format" + "\033[0m")
    if lives == 0:
        print("\033[34m" + f"Word was {word1}" + "\n" "\033[0m")
        time.sleep(1)
        sys.exit("You lose!")


