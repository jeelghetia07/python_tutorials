a = [12,45,32,56,78,93,1,4]    #normal way

# index = 0
# for mark in a:
#     print(mark)
#     if (index == 3):
#         print("okay") 
#     index +=1    



# for index, mark in enumerate(a):   #enumarate allows to lop a sequence and get the index and the value of each element
#     print(mark)
#     if (index == 3):
#         print("okay") 
    
     

for index, mark in enumerate(a, start=1):   #ano meaning e ke index chaluj 1 thi thase...
    print(mark)
    if (index == 3):
        print("okay") 
    



