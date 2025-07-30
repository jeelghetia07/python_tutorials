lst = ['madam', 'Python', "malayalam", 12321]

def is_palindrome(s):
    s = str(s) 
    return s == s[::-1]

for item in lst:
    if isinstance(item, str) and is_palindrome(item):
        print(item)

# madam
# malayalam
