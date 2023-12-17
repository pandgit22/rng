import random

def generate_random_number(min_value, max_value):
    # generate a random number between min_value and max_value.
    return random.randint(min_value, max_value)

if __name__ == "__main__":
    # set the range for the random number.
    min_value = 1
    max_value = 99

    # generate and print a random number.
    random_number = generate_random_number(min_value, max_value)
    print(random_number)

