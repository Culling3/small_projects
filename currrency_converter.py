import re
import requests

while True:
        n = input("List - list of currencies avaliable \nRate - convert a certain amount of initial currency to another \nChoose format: ").lower()
        if n == "rate":
            ic = str(input("Enter the form of initial currency: ")).upper()
            fc = str(input("Enter the form of final currency: ")).upper()
            a = float(input("Enter the amount in initial currency: "))
            response = requests.get(f"https://api.frankfurter.app/latest?amount={a}&from={ic}&to={fc}")
            if o := str(response.json()['rates']):
                o5 = re.split(": |}", o)
                o7 = o5[1]
                print(f"{a} {ic} is {o7} {fc}")
                break
            else:
                raise KeyError("Data for given currency unavailable")

        elif n == "list":
            list = requests.get("https://api.frankfurter.app/latest?")
            list1 = list.json()["rates"]
            list2 = list1.keys()
            x = 0
            for i in list2:
                x += 1
                if x == 15:
                    print(f"{i}", end="\n")


                else:
                    if x == 30:
                        print(f"{i}", end="")
                    else:

                        print(f"{i}, ", end="")

            break
        elif (n != "rate") or (n != "list"):
            TypeError("Invalid format")