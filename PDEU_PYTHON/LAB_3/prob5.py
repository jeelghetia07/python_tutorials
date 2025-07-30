import math
print("Pythagorean Triplets (a,b,c) with side length <= 30")
for a in range(1,31):
    for b in range(a,31):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and c <= 30:
            print(f"{a}, {b}, {int(c)}")

# Output : 
# Pythagorean Triplets (a,b,c) with side length <= 30
# 3, 4, 5
# 5, 12, 13
# 6, 8, 10
# 7, 24, 25
# 8, 15, 17
# 9, 12, 15
# 10, 24, 26
# 12, 16, 20
# 15, 20, 25
# 18, 24, 30
# 20, 21, 29