import time

x = input("Enter your name :")

hour = int(time.strftime("%H"))

if  0 <= hour < 12:
    print("Good Morning", x)

elif 12 <= hour < 16:
    print("Good Afternoon", x)

elif 16 <= hour < 19:
    print("Good Evening", x)

else :
    print("Good Night", x)