a=int(input("Enter the lenght : "))
b=int(input("Enter the breadth : ")) 

area = (a*b)
perimeter = 2*(a+b)

if(area > perimeter):
  print("area is greater")
else:
  print("perimeter is greater")

# Output :
# Enter the lenght : 4
# Enter the breadth : 3
# perimeter is greater