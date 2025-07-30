meals = [("chabhakhri" ,80), ("GujaratiThali", 200), ("TheplaSukiBhaji", 100)]

size = len(meals)

for i in range(size):
    for j in range(size - i -1):
        if meals[j][1] < meals[j+1][1]:
            temp = meals[j]
            meals[j] = meals[j+1]
            meals[j+1] = temp

print(meals)

# Output : 
# [('GujaratiThali', 200), ('TheplaSukiBhaji', 100), ('chabhakhri', 80)]