import random
import time


die = [1,2,3,4,5,6]
yscore = 0
cscore = 0


while True:

    i = str(input("Roll(r) the die or skip(s)? ")).lower()
    if i == "r":
        x = random.choice(die)
        if x == 1:
            print("You rolled a 1.")
            time.sleep(0.5)
            print("You lose!")
            break
        else:
            yscore += x
            print(f"You rolled a {x}!")
            print(f"Your score: {yscore}")
            time.sleep(1)
            print("Computer's turn", end="")
            time.sleep(0.66)
            print(".", end="")
            time.sleep(0.66)
            print(".", end="")
            time.sleep(0.66)
            print(".")
            time.sleep(0.66)
            y = random.choice(die)
            if y == 1:
                print(f"Computer rolled a 1.")
                time.sleep(0.5)
                print(f"You win!")
                break
            else:
                cscore += y
                print(f"Computer rolled a {y}")
                print(f"Computer's score: {cscore}")
                time.sleep(2)
    elif i == "s":
        print(f"You skipped the turn...")
        time.sleep(1.5)
        print("Computer's turn", end="")
        time.sleep(0.66)
        print(".", end="")
        time.sleep(0.66)
        print(".", end="")
        time.sleep(0.66)
        print(".")
        time.sleep(0.66)
        y = random.choice(die)

        if y == 1:
            print(f"Computer rolled a 1.")
            time.sleep(0.5)
            print(f"You win!")
        else:
            cscore += y
            print(f"Computer rolled a {y}")
            print(f"Computer's score: {cscore}"),
            time.sleep(1)

            if cscore == yscore:
                print(f"It's a tie!")
                break
            elif yscore > cscore:
                print(f"You win!")
                break
            else:
                print("You lose!")
                break
