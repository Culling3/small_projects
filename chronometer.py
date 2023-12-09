import time

f = input("seconds(s) or miliseconds(ms)? ").lower()
t = int(input("Enter time to wait: "))


if f == "s":
    for i in range(t + 1):
        if i == 0:
            print("")
        else:
            time.sleep(1)
            print(i, end=" ")
elif f == "ms":
    for c in range(t +1 ):
        if c == 0:
            print("")
        else:
            time.sleep(0.01)
            print(c, end=" ")
