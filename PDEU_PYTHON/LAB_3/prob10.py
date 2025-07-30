n = int(input("enter the position u want the ans : "))
a=0
b=1
print("The fibonacci series is : ")

for i in range(n):
    print(a, end=" ")
    temp = a+b
    a = b
    b = temp

# Output : 
# The fibonacci series is : 
# 0 1 1 2 3 5 8 13 21 34