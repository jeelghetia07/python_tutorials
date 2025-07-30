def count_lower_upper(s):
    counts = {"uppercase": 0, "lowercase": 0}
    
    for i in s:
        if i.isupper():
            counts["uppercase"] += 1
        elif i.islower():
            counts["lowercase"] += 1
    
    return counts

# Sample usage
sample = "Hello World, Jeel Ghetia !!"
result = count_lower_upper(sample)

print("Input String:", sample)
print("Letter Counts:", result)
