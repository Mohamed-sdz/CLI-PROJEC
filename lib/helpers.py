import os
from collections import namedtuple
from lib.db.models import Product, Supplier, Task
from lib.db import session
from ranges import Range
import tuples

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Custom Tuple class
Tuple = namedtuple('Tuple', ['x', 'y'])

# Custom Range class
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Function to get a positive integer input
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer")

 