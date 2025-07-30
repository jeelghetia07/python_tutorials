d1 = {1 : "jeel" , 2 : "fenil" , 3 : "jash"}
d2 = {4 : "cse" , 5 : "civil" , 6 : "cse"}
d3 = {7 : "paubhaji" , 8 : "thepla" , 9 : "panipuri"}

d4 = {**d1,**d2,**d3}
print(d4)

# Output : 
# {1: 'jeel', 2: 'fenil', 3: 'jash', 4: 'cse', 5: 'civil', 6: 'cse', 7: 'paubhaji', 8: 'thepla', 9: 'panipuri'}



# for i, j in d1.items():
#     print(f"{i} : {j}")