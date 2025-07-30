# s = {3,5,8,3,6,8}   #two same items are printed only once
# print(s)

# x = {}  #this is a dictionary
# print(type(x))

# x = set()
# print(type(x))

s1 = {1,2,3,6,7}
s2 = {2,5,4,7,8}
print(s1.union(s2))
s1.update(s2)    #means that s2 ma je value che e badhi s1 ma avi jai
print(s1,s2)
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1.symmetric_difference(s2))  #ama je common nai hoi e badhi print thase
print(s1.difference(s2))      #ama s2 ma je values je s1 ma pn che e badhi s1 mathi nikdi jai
print(s1.isdisjoint(s2))      #ama jo s1 and 2 ma common hoi to e false return krse..ane jo cmn nai oi to e true retur krse


# s1 = {"tokyo","delhi","mumbai","rajkot"}
# s2 = {"ahmedabad","delhi","tokyo"}
# print(s1.issuperset(s2))   #jo s2 ma value je che e pn s1 ma hoi to true return krse
# print(s1.issubset(s2))
# s1.add("Helsinki")
# s1.remove("tokyo2")   #this can raise an error
# s1.discard("tokyo2")   #but this will not raise any error
# x = s1.pop()    #randomly it pops any value
# del s1   #this means that it deletes all the set s1
# s1.clear() #this just clears the items in the set
# print(s1)