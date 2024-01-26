# Importing modules
import math
import random
import datetime  # Additional import for date and time

# function that performs  computation
def calculate_square_root(number):
    return math.sqrt(number)

# function that generates a random number
def generate_random_number():
    return random.randint(1, 100)

# function to get the current date and time
def get_current_datetime():
    return datetime.datetime.now()

def main():
    # Example usage of the defined functions
    input_number = 25
    result = calculate_square_root(input_number)
    print(f"The square root of {input_number} is: {result}")

    random_num = generate_random_number()
    print(f"Generated random number: {random_num}")

    current_datetime = get_current_datetime()
    print(f"Current date and time: {current_datetime}")

#  conditional execution logic
if __name__ == "__main__":
   
    main()
