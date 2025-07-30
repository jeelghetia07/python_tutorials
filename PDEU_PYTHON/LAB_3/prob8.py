n = int(input("Enter the number : "))
fact = 1

for i in range(1 , n+1):
    fact *= i
    
print(f"Factorial = {fact}")

# Output : 
# Enter the number : 5
# Factorial = 120