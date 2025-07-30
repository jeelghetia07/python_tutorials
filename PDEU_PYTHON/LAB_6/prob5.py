list = [(5,), (9,),() , (8,),(10,),(),(),(18,)]
print("original list : ",list)

new_list = [i for i in list if i]
print("final list : ",new_list)

# Output : 
# original list :  [(5,), (9,), (), (8,), (10,), (), (), (18,)]
# final list :  [(5,), (9,), (8,), (10,), (18,)]