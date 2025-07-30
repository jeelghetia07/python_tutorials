a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

if a>b and a>c:
  print(f"{a} is the biggest number")
elif b>a and b>c:
  print(f"{b} is the biggest number")
else:
  print(f"{c} is the biggest number")

# Output :
# a = 4  
# b = 9
# c = 5
# 9 is the biggest number