def marks(a,b,c,d,e):
    total = (a+b+c+d+e)
    avg = total / 5
    return total, avg

total_marks ,avg_marks = marks(89,95,97,68,67)

print("The total marks is : ", total_marks)
print("The average marks is : ", avg_marks)