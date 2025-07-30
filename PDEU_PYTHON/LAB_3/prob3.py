str = "jeel123"
digit_count = 0
char_count = 0
for i in str:
    if  '0' <= i <= '9':
        digit_count += 1
    elif 'A' <= i <= 'z':
        char_count += 1

print("the digits are : " , digit_count)
print("the chars are : " , char_count)

# Output : 
# the digits are :  3
# the chars are :  4
