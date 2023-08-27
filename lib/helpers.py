import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_positive_integer_input(prompt):
      """Prompts the user for a positive integer input."""
      while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
