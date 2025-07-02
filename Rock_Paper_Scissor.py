import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("enter your move = Rock, Paper, Scissor = ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer  choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both choose same: Match tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("paper cover Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cut paper = Computer Win")
    else:
        print("paper cover Rock = You Win")

elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cut paper = You Win")
    else:
        print("Rock smashes Scissor = Computer Win")