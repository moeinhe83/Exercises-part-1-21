# Practice_21

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 21', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value
l1 = ['python', 'java']
l2 = ['c#']

# Merge lists
l1.extend(l2)
print(l1)

# Finish
# Create By Moein Heshmati
