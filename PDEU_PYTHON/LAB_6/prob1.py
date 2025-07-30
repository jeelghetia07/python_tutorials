list = [("manav",) , ("jeel",) , ("dharam",) , "priya" , "khushi"]
boys = []
girls = []

for i in list:
    if isinstance(i,tuple):
        boys.append(i[0])
    else:
        girls.append(i)

print(boys)
print(girls)

# Output : 
# ['manav', 'jeel', 'dharam']
# ['priya', 'khushi']