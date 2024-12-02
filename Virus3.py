import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Birthday Cake ASCII Art
cake_art = """
         ,   ,   ,
       , |_,_|_,_| ,  
       |   Happy    |
   ,   |   Birthday  |   ,
   | |_|_,_|_,_|_,_|_| |
   |   ,   ,   ,   ,   |
   |_|_|_|_|_|_|_|_|_|_|
   |   ,   ,   ,   ,   |
   | |_|_,_|_,_|_,_|_| |
   |___________________|
"""

# Compact ASCII Art for "HAPPY BIRTHDAY MIDHUN"
ascii_text = """
H A P P Y   B I R T H D A Y
        M I D H U N
"""

# Colors to cycle through
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA]

# Multi-Color Flashing Effect for Cake and Text
def multi_color_flash(cake, text, duration=20, delay=0.2):
    start_time = time.time()
    while time.time() - start_time < duration:
        for color in colors:
            os.system("clear")
            print(color + Style.BRIGHT + cake)  # Flashing cake
            print(color + Style.BRIGHT + text)  # Flashing text
            time.sleep(delay)

# Main function to display the program
def birthday_program():
    os.system("clear")
    
    # Flashing multi-color cake and ASCII art for 20 seconds
    multi_color_flash(cake_art, ascii_text, duration=20, delay=0.2)
    
    # Final birthday message
    os.system("clear")
    print(Fore.MAGENTA + Style.BRIGHT + cake_art)
    print(Fore.CYAN + Style.BRIGHT + ascii_text)
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT + "HAPPY BIRTHDAY  MACHA MIDHUN!")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "ATHA MIND BIRTHDAY MIND EH")

# Run the program
if __name__ == "__main__":
    birthday_program()

