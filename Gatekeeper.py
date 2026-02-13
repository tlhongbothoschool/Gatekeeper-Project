"""
Tlhong-Botho J O O Nkile

HNC/HND Digital Technologies

Campus Quest Mini Game

Unlock Location 1: The Learning Resource Centre

Mini-game name: The Gatekeeper

The requirement: The LRC is a place of focus and logic. You will build a Number Bonds game. Players (students) must demonstrate quick mental arithmetic to crack the code and enter the quiet study zone.
"""

import random
import time
import sys

#FUNCTIONAL
def get_valid_number():
    """Get a valid whole number from the user with time tracking.
    
    Returns:
        int: The validated number entered by the user
    """
    while True:
        try:
            start_time = time.time()  # timer
            print("Number = ")
            number = int(input())  # the users numbers
            end_time = time.time()  # end of timer
            elapsed_time = end_time - start_time  # elapsed time
            print(f"You took {elapsed_time:.2f} seconds")
            return number
        except ValueError:
            print("Error: Please enter a whole number")
#FUNCTIONAL

# target determination
target = random.randint(10, 99) 

# intro to game
print("Welcome to the Campus Quest The Gatekeeper Mini-game.")
print(f"To unlock the LRC you need {target}.\n")

# number of additions to be made
num_bonds = random.randint(3, 6) 
print(f"Use {num_bonds} in total to make {target}")
#PROCEDURAL
# creates a list to store each bond given by the user
numbers = [] 
while num_bonds != 0:
    # Get valid number using the function
    Number = get_valid_number()
    
    numbers.append(Number)  # add input to the list (OOP)
    print(f"Current numbers: {numbers}")
    print(f"You are left with {num_bonds-1} to make {target}")  # tracker for the user
#PROCEDURAL    
    num_bonds -= 1  # leave the loop after x amount of numbers


sum_of_Numbers = sum(numbers)  # sum of list
print(f"Your sum is {sum_of_Numbers} while the the target is {target}")

tries = 5  # {joke} permanently lock them out
if abs(sum_of_Numbers - target) <= 3:  # tolerance of 3 points
    print("Correct. The LRC will now be unlocked.")
else:
    print(f"Incorrect. You Have {tries - 1} left.")
    sys.exit()  # end
