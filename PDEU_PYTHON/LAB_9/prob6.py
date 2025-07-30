def generate_tuples(end):
    return [(x, x**2, x**3) for x in range(1, end + 1)]

print(generate_tuples(5))  

# Output :
# [(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]