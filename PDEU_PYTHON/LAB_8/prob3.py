s1 = set()

s1.update({"jeel" , "manav" , "dharam","khush", "jay"})
print("new set after adding the elements : ",s1)

if "manav" in s1:
    s1.remove("manav")
    s1.add("raj")

print("Modified set : ", s1)

s1.discard("jeel")
s1.discard("dharam")

print("last set : ", s1)

# Output : 
# new set after adding the elements :  {'jay', 'khush', 'manav', 'dharam', 'jeel'}
# Modified set :  {'jay', 'khush', 'raj', 'dharam', 'jeel'}
# last set :  {'jay', 'khush', 'raj'}