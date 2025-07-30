import random as rd

rd_list = [rd.randint(1,30) for _ in range(50)]
print("The original list is : " , rd_list)

new_list= list(set(rd_list))
print(new_list)

# Output : 
# The original list is :  [19, 30, 22, 15, 16, 28, 12, 19, 26, 1, 15, 22, 14, 18, 26, 21, 18, 30, 6, 17, 7, 27, 11, 21, 2, 13, 8, 12, 6, 16, 21, 29, 5, 28, 23, 29, 9, 16, 21, 14, 22, 23, 29, 7, 4, 18, 29, 29, 18, 27]
# [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 26, 27, 28, 29, 30]