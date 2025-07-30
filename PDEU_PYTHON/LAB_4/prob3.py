str1 = input("Enter string 1 here : ")
str2 = input("Enter string 2 here : ")
present = False

for i in range(len(str1) - len(str2) + 1):
    if str1[i : i + len(str2)] == str2:
        present = True
        break
    else:
        present = False

if present == True:
    print("yes its present")
else:
    print("Not present")

# Output : 
# Enter string 1 here : Hello
# Enter string 2 here : lo
# yes its present