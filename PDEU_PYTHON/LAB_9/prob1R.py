def prime_factors(n, divisor=2):
    if n <= 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

n = int(input("Enter a positive integer: "))
print("Prime factors:", prime_factors(n))

# Input: 60
# Output: [2, 2, 3, 5]

