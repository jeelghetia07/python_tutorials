str1 = input("Enter string 1 here : ")
strrem = input("Enter string to remove here : ")
result_str = ""
i = 0

while i < len(str1):
    if str1[i : i + len(strrem)] == strrem:
        i += len(strrem)
    else:
        result_str += str1[i]
        i+=1

print(f"Final String is : {result_str}")

# Output :
# Enter string 1 here : jeel
# Enter string to remove here : e
# Final String is : jl