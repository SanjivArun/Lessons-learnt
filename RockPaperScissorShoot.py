import random

possible_user_respond = ["Rock", "Paper", "Scissors"]
possible_com_respond = random.choice(possible_user_respond)


def conditions(com_response, user_response):
    # User ties
    if com_response == "Scissors" and user_response == "Scissors":
        print("Tie!")
    elif com_response == "Rock" and user_response == "Rock":
        print("Tie!")
    elif com_response == "Paper" and user_response == "Paper":
        print("Tie!")
    # User loses
    elif com_response == "Scissors" and user_response == "Paper":
        print("You Lose!")
    elif com_response == "Paper" and user_response == "Rock":
        print("You Lose!")
    elif com_response == "Rock" and user_response == "Scissors":
        print("You Lose!")
    # User wins
    elif com_response == "Scissors" and user_response == "Rock":
        print("You Win!")
    elif com_response == "Paper" and user_response == "Scissors":
        print("You Win!")
    elif com_response == "Rock" and user_response == "Paper":
        print("You Win!")


print("Welcome to Rock, Paper, Scissor, SHOOT!")
print("Let us start playing!")
print("Choices: ", possible_user_respond)
user_input = str(input("Input your choice: "))
print("COMPUTER response: ", possible_com_respond)
conditions(possible_com_respond, user_input)
