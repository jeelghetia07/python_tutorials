import math as mt

n = int(input("Enter the total students 'n' : "))
r = int(input("Enter the r : "))

nPr = mt.factorial(n) / mt.factorial(n-r)
nCr = mt.factorial(n) / (mt.factorial(r) * mt.factorial(n-r))

print(f"The nPr is : {nPr}")
print(f"The nCr is : {nCr}")

# Output : 
# Enter the total students 'n' : 5
# Enter the r : 3
# The nPr is : 60.0
# The nCr is : 10.0