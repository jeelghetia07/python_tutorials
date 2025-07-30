s = input("Enter a string: ")
freq = {}

for i in s:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1   

print("Character Frequency:", freq)

# Output : 
# Enter a string: jeel
# Character Frequency: {'j': 1, 'e': 2, 'l': 1}