faculty_names = ["Dr. Sharma", "Prof. Mehta", "Annapurna", "Christopher", "Amy", "Jonathan"]

long_names = [name for name in faculty_names if len(name) > 8]

print("Faculty names with more than 8 characters:")
for name in long_names:
    print(name)

# Faculty names with more than 8 characters:
# Prof. Mehta
# Annapurna
# Christopher
# Jonathan
