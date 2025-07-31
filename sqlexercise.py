import os

filename = "sqltest.txt"

def create():
    roll_no = int(input("enter roll number : "))
    name = input("enter name : ")
    age = int(input("enter age : "))
    department = input("enter department : ")
    with open(filename, 'a') as file:
        file.write(f"{roll_no} , {name} , {age} , {department}\n")
        print("Record added.")

def read():
    with open(filename,'r') as file:
        lines = file.readlines()
        print("the data is : ")
        for l in lines:
            parts = [p.strip() for p in l.strip().split(',')]
            if len(parts) == 4:
                roll_no, name, age, department = parts
                print(f"Roll no : {roll_no}, Name : {name}, Age : {age}, Department : {department}\n")


while True:
    print("------ MENU ------")
    print("1. Create ")
    print("2. Read ")
    print("3. Exit")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again!\n")