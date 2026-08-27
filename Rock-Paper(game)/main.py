"""
Workflow of project:
1- Input from user(rock, paper, scissor)
2- cmp will chose randomly not canditionally
3- result prt

cases:
A- Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = rock win

B- Paper
paper - paper = tie
paper - rock = paper win
paper - scissor = scissor win

c - scissor 
scissor - scissor = tie
scissor - rock = rock win
scissor - paper = scissor win

"""
import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, paper, Scissor = ")
cmp_choice = random.choice(item_list)

print(f"User Choice =  {user_choice}, Computer choice = {cmp_choice}")

if user_choice == cmp_choice:
    print("Both choose same: Match Tie")
elif user_choice == "Rock":
    if cmp_choice == "Paper":
        print("Paper covers Rock = Computer")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if cmp_choice == "Scissor":
        print("Scissor cuts paper, Computer win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "Scissor":
    if cmp_choice == "Paper":
        print("Scissor cuts paper, You Win")
    else:
        print("Rock smashes scissor, Computer Win")