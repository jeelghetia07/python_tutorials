str1 = input("Enter a string : ")
vowel = "aeiouAEIOU"
count = 0

for i in str1:
    if i in vowel:
        count += 1

print(f"The vowels in string are {count}")

# Output : 
# Enter a string : abcdefghijklmnopqrstuvxyz
# The vowels in string are 5