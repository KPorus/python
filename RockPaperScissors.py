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
        print("ohh Tie!!!")
    elif player == "rock":
        if computer == "paper":
            print("paper cover rock. you loose!!")
        else:
            print("rock break the scissors. you win!!")
    elif player == "paper":
        if computer == "rock":
            print("paper cover rock. you win!!")
        else:
            print("scissors cut paper. you loose!!")
    elif player == "scissors":
        if computer == "rock":
            print("rock break scissors. you loose!!")
        else:
            print("scissors cut paper. you win!!")


while 1:
    option = choices();
    winner(option['player'], option['computer'])
    a= int(input("Want to exit than press 0 or countinu press 1: "))
    if a == 0:
        break
    elif a == 1:
        option = choices();
        winner(option['player'], option['computer'])