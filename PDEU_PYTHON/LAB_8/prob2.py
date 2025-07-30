import random as rd

numbers = set()

for _ in range(10):
    numbers.add(rd.randint(15,45))

print("Final set : ", numbers)

count = 0
for i in numbers:
    if i < 30:
        count += 1
print("numbers less than 30 : ",count)

new_numbers = set()
for i in numbers:
    if i < 35:
        new_numbers.add(i)

print("Numbers after removing those > 35:", new_numbers)

# Output : 
# Final set :  {37, 41, 45, 15, 17, 19, 22, 26, 31}
# numbers less than 30 :  5
# Numbers after removing those > 35: {15, 17, 19, 22, 26, 31}
