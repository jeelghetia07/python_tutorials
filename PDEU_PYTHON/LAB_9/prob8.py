def convert(s):
    words = s.split()
    unique_sorted = sorted(set(words))
    return ' '.join(unique_sorted)

print(convert("hello world hello python world"))  

# Output :
# 'hello python world'