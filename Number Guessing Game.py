import random
import colorama
from colorama import Fore, Style


num = random.randint(1, 10)

guess = 0
while guess != num:
  guess = int(input("Guess a number between 1 and 10: "))
  if guess == num:
    print(Fore.GREEN + "You Win! " + Style.RESET_ALL)
  else:
    print(Fore.RED + "You Lose! Try again! " + Style.RESET_ALL)