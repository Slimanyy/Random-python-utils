from random import randint


def verify(hand):
    if hand < 0 or hand > 2:
        return False
    return True


def printhand(hand, name):
    handsigns = ["Rock", "Paper", "Scissors"]
    print(name + " picked " + handsigns[hand])


def winner(user, Slimany_AI):
    if Slimany_AI == user:
        return "IT HAS END IN A DRAW"
    elif user == 0 and Slimany_AI == 1:
        return "You Lose, SLIMANY ADVANCED AI Wins"
    elif user == 2 and Slimany_AI == 0:
        return "You Lose, SLIMANY ADVANCED AI Wins"
    elif user == 1 and Slimany_AI == 2:
        return "You Lose, SLIMANY ADVANCED AI Wins"
    else:
        return user_name + " Wins"


# e = 1
# while e < 10:
#   e += 1


print('''ROCK  PAPER SCISSORS 
                                                    by SLIMANY STUDIOS''')
user_name = input("Enter your name: ")  # "Slimany"
user_hand = int(input('''Choose
 0 for Rock
 1 for Paper
 2 for scissors
 Enter preferred choice: '''))
#0

if verify(user_hand):
    computer = randint(0, 2)

    printhand(user_hand, user_name)

    printhand(computer, "SLIMANY ADVANCED AI")

    result = winner(user_hand, computer)

    print(result)
else:
    print("Please choose a valid hand")
