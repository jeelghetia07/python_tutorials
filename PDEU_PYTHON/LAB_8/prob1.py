ls = ["jeel", "manav" , "dharam"]
new_set = {i.upper() for i in ls}
new_set = set(i.upper() for i in ls)
print(new_set)

# Output :
# {'DHARAM', 'JEEL', 'MANAV'}