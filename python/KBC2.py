import time

x = input("Please enter you're name sir/mam : ")
hour = int(time.strftime("%H"))

if 0 <= hour <= 12:
    print("\nGood Morning",x)

elif 12 < hour <= 16:
    print("\nGood Afternoon",x)    

elif 16 < hour <= 20:
    print("\nGood Evening",x)

else:
    print("\nGood Night",x)        

print("\nWelcome Back To Kaun Banega Crorepati......")
print("\n So Let's Begin......")

que = ["\n1). What is the value of g ?\nA : 9.8\nB : 9.9\nC : 10\nEnter the option here : ",
       "\n2). In what year did we land in India ?\nA : 2017\nB : 2016\nC : 2015\nEnter the option here : "]
ans = ["A","B"]

points = [1000,2000]

que1 = input(que[0])

if que1 == ans[0] :
  print("Great ans,YOU HAVE WON", points[0],"INR")

else :
    print("Galat Jawab")  

que2 = input(que[1])

if que2 == ans[1] :
  print("Great ans,YOU HAVE WON", points[1],"INR")

else :
    print("Galat Jawab")    

