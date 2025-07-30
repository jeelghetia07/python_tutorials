num_word = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen"}

n = int(input("enter the number : "))

if 0 <= n <= 19:
    print(f"{n} --> {num_word[n]}")
else:
    print("invalid")

# Output :
# enter the number : 9
# 9 --> nine