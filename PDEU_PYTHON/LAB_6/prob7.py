tup = (9,18,27,36,45,54,63,72,81,90)
target = 36
tup2list = list(tup)

a = [i for i in tup2list if i != target]
new_tup = tuple(tup2list)

print(new_tup)

# Output : 
# [9, 18, 27, 45, 54, 63, 72, 81, 90]