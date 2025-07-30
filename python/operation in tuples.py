fruits = ("mango","apple","pineapple","strawberry")

temp = list(fruits)
temp.append("guava")     #add item
temp.pop(0)              #remove item
temp[1] = "banana"       #change item
print(temp)
fruits = tuple(temp)
print(fruits)


# tuple1 = (1,2,3,2,3,1,2,3,1,4,5)
# x = tuple1.count(4)
# x = tuple1.index(3)
# print("The count is :" , x)