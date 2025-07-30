import math

x=int(input("x : "))
y=int(input("y : "))
a=int(input("Centre of circle a : "))
b=int(input("Centre of circle b : "))
r=int(input("radius : "))

d = math.sqrt(pow((x-a),2) + pow((y-b),2))     # this is the distance formula..for calc the dis btw 2 points..

if  d == r :
             print("on the circle")
elif  d > r :
             print("outside the circle")
else:
             print("inside the circle")

# Output :
# x : 4
# y : 5
# Centre of circle a : 6
# Centre of circle b : 4
# radius : 7
# inside the circle
