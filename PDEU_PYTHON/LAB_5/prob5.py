far_list = [100, 150,200]
cel_list = []

for f in far_list:
    c = (f-32 * (5/9))
    cel_list.append(c)

print(cel_list)

# Output : 
# [82.22222222222223, 132.22222222222223, 182.22222222222223]