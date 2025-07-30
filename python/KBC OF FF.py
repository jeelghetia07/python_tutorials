import time as t

x = input("\t\nEnter your name :")

hour = int(t.strftime("%H"))

if 0 <= hour < 12:
    print("\t\n--> Good Morning", x)

elif 12 <= hour < 16:
    print("\t\n--> Good Afternoon", x)

elif 16 <= hour < 20:
    print("\t\n--> Good Evening", x)

elif 20 <= hour < 24:
    print("\t\n--> Good Night", x)

print("\n Welcome Back in Kau Banega Free Fire Ka Crorepati")
print("\nSo..Let's Begin...\n")

que = ["\t\n1). What year was free fire released ?\nA: 2017\nB: 2018\nC: 2019\nD: 2020\nEnter the option here :","2). Who is the fastest character in 2020 ?\nA: Tatsuya\nB: Santino\nC: DJ Alok\nD: Kla\nEnter the option here :","3). Which gun has an emote like thor ?\nA: AK47\nB: MP40\nC: SCAR\nD: MP5\nEnter the option here :","4). Which creator has the most no. of subscribers? \nA: Gyan Gaming\nB: Techno Gamerz\nC: Desi Gamers\nD: Total Gaming\n Enter the option here :\n"]
ans = ["A","C","A","D"]
lifeline = ["Kya ap lifeline lena chahoge ?"]
lifelineAns = ["yes","no"]

a = 1000
b = 2000
c = 3000
d = 4000

que1 = input(que[0])

if que1 == ans[0]:
    print("\nYou have won", a,"Diamonds !!!!\n")
else :
    print("Galat Jawab....")
    lifeline = input(lifeline[0])

    if lifeline == lifelineAns[0]:
        print(" \nThe ans is A\n")
    else :
        print("\nItna bhi nhi ata tumhe...satvi fail..\n")


que2 = input(que[1])
if que2 == ans[1]:
    print("You have won", b,"Diamonds !!!!\n")
else :
    print("Galat Utar....")
    lifeline = input(lifeline[0])

    if lifeline == lifelineAns[0]:
        print(" \nThe ans is C\n")
    else:
        print("\nItna bhi nhi ata tumhe...satvi fail..\n")


que3 = input(que[2])
if que3 == ans[2]:
    print("You have won", c,"Diamonds !!!!\n")
else :
    print("Galat Utar....")
    lifeline = input(lifeline[0])

    if lifeline == lifelineAns[0]:
        print(" \nThe ans is A\n")
    else:
        print("\nItna bhi nhi ata tumhe...satvi fail..\n")



que4 = input(que[3])
if que4 == ans[3]:
    print("You have won", d,"Diamonds !!!!\n")
else :
    print("Galat Utar....")
    lifeline = input(lifeline[0])

    if lifeline == lifelineAns[0]:
        print(" \nThe ans is D\n")
    else:
        print("\nItna bhi nhi ata tumhe...satvi fail..\n")



print("\nChalo", x, "Milte he apse kuch wakht ke baad!!, ye rha reedem code...DUE4EDJI453NNUE34O4" )
