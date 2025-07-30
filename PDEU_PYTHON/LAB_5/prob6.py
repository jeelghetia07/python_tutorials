l1 = [2,5,4,1,3,6]
l2 = [1,4,6,3]
l3 = []

for i in l1:
    if i not in l2:
        l3.append(i)

print("those numbers from first list which are not there in 2nd list are :  ",l3)

# Output :
# those numbers from first list which are not there in 2nd list are :   [2, 5]