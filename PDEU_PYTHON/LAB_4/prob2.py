str1 = input("Enter a string : ")
lower = ""

for i in str1:
    if 'A' <= i <= 'Z':
        lower += chr(ord(i) + 32)
    elif 'a' <= i <= 'z':
        lower += chr(ord(i) - 32)
    else:
        lower += i

print(f"Final String is : {lower}")

# Output
# Enter a string : jEEl
# Final String is : JeeL