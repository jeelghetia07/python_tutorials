def count_vowels(s):
    if not s:
        return 0
    return (s[0].lower() in 'aeiou') + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))

# Input: "Recursion is awesome"
# Output: 8
