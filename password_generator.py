import random
o = "1234567890.,*'^+%&/()=#:;$½{[]}-_+`<>qwertyuopasdfghjklizxcvbnméQWERTYUOPASDFGHJKLIZXCVBNM"
a = "QWERTYUOPASDFGHJKLIZXCVBNM"
b = "qwertyuopasdfghjklizxcvbnmé"
c = ".,*'^+%&/()=#:;$½{[]}-_+`<>"
d = "1234567890"

while True:
    e = int(input("How many characters do you want your password to be? (min 8 characters): "))
    if 8 <= e:
        break
    else:
        pass

def random1(o):
    z = ""
    for i in range(e):
        z += random.choice(o)
    return z

def che(o, k):
    for i in o:
        for z in k:
            if z == i:
                return True
            else:
                pass
    return False


while True:

    z = random1(o)
    k = che(z, a)
    l = che(z, b)
    m = che(z, c)
    n = che(z, d)
    if (k and l and m and n):
        print(z)
        break
    else:
        pass