def count_alpha_digits(s):
    result = {'alphabets': 0, 'digits': 0}
    for char in s:
        if char.isalpha():
            result['alphabets'] += 1
        elif char.isdigit():
            result['digits'] += 1
    return result

print(count_alpha_digits("abc123xyz"))  

# Output :
# {'alphabets': 6, 'digits': 3}