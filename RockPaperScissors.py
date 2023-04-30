import random

def choices():
    option = ["rock","paper","scissors"];
    com_choice = random.choice(option)
    player_choice = input("enter your choice (rock, paper, scissors): ").lower();
    choice = {"player":player_choice,"computer":com_choice}
    return choice;
def winner(player,computer):
    print(f"your choice is {player} and computer choice is {computer}")
    if player == computer:
        return print("ohh Tie!!!")
    elif player == "rock":
        if computer == "paper":
            return print("paper cover rock. you loose!!")
        else:
            return print("rock break the scissors. you win!!")
    elif player == "paper":
        if computer == "rock":
            return print("paper cover rock. you win!!")
        else:
            return print("scissors cut paper. you loose!!")
    elif player == "scissors":
        if computer == "rock":
            return print("rock break scissors. you loose!!")
        else:
            return print("scissors cut paper. you win!!")

while 1:
    option = choices();
    winner(option['player'], option['computer'])