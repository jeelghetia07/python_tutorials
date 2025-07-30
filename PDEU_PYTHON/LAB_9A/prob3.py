import random

random_numbers = random.sample(range(-15, 16), 10)

squared_numbers = list(map(lambda x: x ** 2, random_numbers))

# Print the results
print("Random Numbers:", random_numbers)
print("Squared Numbers:", squared_numbers)
