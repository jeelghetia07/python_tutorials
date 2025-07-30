import random as rd

odd_list = [rd.randrange(1,100,2) for _ in range(5)]
print("Original odd list : ", odd_list)

even_list = [rd.randrange(2,100,2) for _ in range(4)]
print("Original odd list : ", even_list)

odd_list[2] = even_list
print("New Modified odd list : ", odd_list)

flattend_list = []
for i in odd_list:
    if isinstance(i,list):
        flattend_list.extend(i)
    else:
        flattend_list.append(i)
print("Flattened list : ",flattend_list)

flattend_list.sort()
print("sorted list : ", flattend_list)

# Output :
# Original odd list :  [83, 21, 9, 57, 53]
# Original even list :  [68, 64, 56, 66]
# New Modified odd list :  [83, 21, [68, 64, 56, 66], 57, 53]
# Flattened list :  [83, 21, 68, 64, 56, 66, 57, 53]
# sorted list :  [21, 53, 56, 57, 64, 66, 68, 83]