import colorama
from colorama import Fore, Style

temp = float(input("What's the temperature? "))

unit = str(input("Is that in Celcius or Farenheight? "))

if unit.upper() == "CELCIUS" or unit.upper() == "C":
  print(Fore.GREEN + "The temperature in Farenheight is " + str(temp * 1.8 +32) + Fore.RESET)

elif unit.upper() == "FARENHEIGHT" or unit.upper() == "F":
  print(Fore.GREEN + "The temperature in Celcius is " + str((temp - 32) / 1.8) + Fore.RESET)

else:
  print(Fore.RED + "Error, please check your spelling and try again." + Fore.RESET)

