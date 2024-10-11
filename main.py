import time
from colorama import *

init(autoreset=True)

def getage():
    correct = False
    while correct != True:
        try:
            age = int(input(Fore.CYAN + "enter your age 7-13 "))
            if age < 7 or age > 13:
                print(Fore.RED + "not the correct range\n")
                correct = False
            else:
                correct = True
        except ValueError:
            print(Fore.RED + "i asked for an integer! \n")
    return age

age1 = getage()
age2 = getage()
age3 = getage()
age4 = getage()
age5 = getage()

sum = age1 + age2 + age3 + age4 + age5

diff = max(age1, age2, age3, age4, age5) - min(age1, age2, age3, age4, age5)

print(Fore.CYAN + f"The total age is {sum} and the differnce is {diff}")

time.sleep(5)
