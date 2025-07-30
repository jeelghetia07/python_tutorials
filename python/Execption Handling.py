a = input("Enter the number here: ")
print(f"multiplication table for {a} is :")

try:       #a try varu use krine jo apde run kre to error raise na kre
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invaid Input!!")

print("end of the program")