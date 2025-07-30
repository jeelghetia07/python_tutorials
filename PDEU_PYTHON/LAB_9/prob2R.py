def to_binary(n):
    if n == 0:
        return ''
    return to_binary(n // 2) + str(n % 2)

n = int(input("Enter a positive integer: "))
binary = to_binary(n)
print("Binary equivalent:", binary if binary else "0")

# Input: 13
# Output: 1101
