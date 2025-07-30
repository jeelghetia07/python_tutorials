import random as rd

rd_list = [rd.randint(-15,15) for _ in range(30)]
print("The original list is : " , rd_list)

pos_list = [val for val in rd_list if val > 0]
neg_list = [val for val in rd_list if val < 0]

print(pos_list)
print(neg_list)

# Output : 
# The original list is :  [-11, 11, -5, 1, -2, -14, -2, -1, 9, 0, 6, 4, 0, -9, 5, 13, 14, 6, -13, -6, -9, 2, 15, -14, 14, -15, -15, 12, -11, 6]
# [11, 1, 9, 6, 4, 5, 13, 14, 6, 2, 15, 14, 12, 6]
# [-11, -5, -2, -14, -2, -1, -9, -13, -6, -9, -14, -15, -15, -11]