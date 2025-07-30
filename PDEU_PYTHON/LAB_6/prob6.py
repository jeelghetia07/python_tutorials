tup = (9,18,27,36,45,54,63,72,81,90)
newval = 99
index = 3

tup2list = list(tup)

for i in range(len(tup2list)):
    for j in tup2list :
        if i == index :
            tup2list[i] = newval

print(tup2list)


# a=list(tup)
# a[3] = 100
# print(tuple(a))
