x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))
x3 = int(input("Enter x3 : "))
y3 = int(input("Enter y3 : "))

slope1 = (y2-y1) / (x2-x1)
slope2 = (y3-y2) / (x3-x2)
slope3 = (y3-y1) / (x3-x1)

if(slope1 == slope2 == slope3):
  print("are on same line.")
else:
  print("not on same line.")

# Output :
# Enter x1 : 3
# Enter y1 : 4
# Enter x2 : -2
# Enter y2 : -1
# Enter x3 : 9
# Enter y3 : 2
# not on same line.