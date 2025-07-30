s1 = {"Ayush", "Bachan" , "Arpit" , "Bhavya"}
A1 = set()
B1 = set()

for i in s1:
    if i[0] == "A":
        A1.add(i)
    if i[0] == "B":
        B1.add(i)

print(A1)
print(B1)

# Output:
# {'Arpit', 'Ayush'}
# {'Bhavya', 'Bachan'}