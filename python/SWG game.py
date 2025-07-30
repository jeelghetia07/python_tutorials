import random 

response1 = ["snake", "water", "gun"]
response2 = ["s", "w", "g"]
print("Welcome to the 'Snake - Water - Gun' game.")
status = True

decide_rounds = int(input("How many rounds you wish to play : "))
rounds = 1
user_win = 0
comp_win = 0

prompt = "\nType 's' for snake , 'w' for water , 'g' for gun.\n"
prompt += "So what's your response : "

prompt2 = "\nWould you like to play the game? (y/n) : "
while status:
    play_or_not = input(prompt2)
    if play_or_not == "y":
        while rounds <= decide_rounds:
            user_response = input(prompt)

            if user_response not in response2:
                print("Incorrect input,please check your input.")
                # user_response = input(prompt)
                continue

            computer = random.choice(response2)
            print(f"\nComputer chose: {computer} and you chose: {user_response}")
            if computer == 's':
                # print(f"Computer chose: {computer} and you chose: {user_response}")
                if user_response == 'w':
                    comp_win += 1
                    print("Computer wins this round!")
                elif user_response == 'g':
                    user_win += 1
                    print("You win this round!")
                else:
                    print("It's a draw.")
            elif computer == 'w':
                if user_response == 'g':
                    comp_win += 1
                    print("Computer wins this round!")
                elif user_response == 's':
                    user_win += 1
                    print("You win this round!")
                else:
                    print("It's a draw.")
            elif computer == 'g':
                if user_response == 's':
                    comp_win += 1
                    print("Computer wins this round!")
                elif user_response == 'w':
                    user_win += 1
                    print("You win this round!")
                else:
                    print("It's a draw.")

            rounds += 1

        if user_win > comp_win:
            print("\nCongratulations! You Won")
        elif comp_win > user_win:
            print("\nYou lose!")
        else:
            print("\nMatch Draw!")
    elif play_or_not == "n":
        status = False
        print("Hope you loved this project!")

