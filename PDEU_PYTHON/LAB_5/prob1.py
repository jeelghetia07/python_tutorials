import random as rd

rd_list = [ rd.randint(1,10) for _ in range(20)]  # 
print("the list is : ",rd_list)

num = int(input("Enter the number : "))
pos = [i for i,val in enumerate(rd_list) if val == num]

print(pos)

# Output : 
# the list is :  [10, 4, 2, 5, 6, 5, 6, 7, 6, 9, 10, 7, 6, 1, 1, 8, 1, 2, 3, 2]
# Enter the number : 5
# [3, 5]