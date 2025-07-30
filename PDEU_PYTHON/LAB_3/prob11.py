import math

x = float(input("Enter x : "))
terms = 3  # Number of terms in the series

sin_x = 0
for n in range(terms):
    sin_x += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

print("sin(x) using Taylor series:", sin_x)
print("sin(x) using math.sin:", math.sin(x))
