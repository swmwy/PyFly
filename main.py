from colorama import Fore, Back, Style
import flying
import game
import setup
import time

print("Welcome")
time.sleep(1)
print("to")
time.sleep(1)

def output_letters():
  letter = "P"
  if letter == "P":
    next_letter = "y"
    print(Fore.RED + letter)
    time.sleep(1.5)
    if next_letter == "y":
      letter = "y"
      if letter == "y":
        next_letter = "F"
        print(Fore.YELLOW + letter)
        time.sleep(1.5)
        if next_letter == "F":
          letter = "F"
          if letter == "F":
            next_letter = "l"
            print(Fore.GREEN + letter)
            time.sleep(1.5)
            if next_letter == "l":
              letter = "l"
              if letter == "l":
                next_letter = "y"
                print(Fore.BLUE + letter)
                time.sleep(1.5)
                if next_letter == "y":
                  letter = "y"
                  if letter == "y":
                    next_letter = "!"
                    print(Fore.MAGENTA + letter)
                    time.sleep(1.5)
                    if next_letter == "!":
                      letter = "!"
                      if letter == "!":
                        next_letter = "!"
                        print(Fore.CYAN + letter)
                        time.sleep(1.5)
                        print(Style.RESET_ALL)
                  
output_letters()
setup.setup()