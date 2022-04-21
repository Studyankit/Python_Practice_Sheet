import random


def Gambling_Game(stake, goal, win_check=0, loss_check=0):
    win_amount = 0
    while win_amount <= goal and stake != 0:
        player_turn = random.randint(0, 3)
        if player_turn == 1:
            goal -= 1
            stake -= 1
            win_check += 1
        else:
            stake -= 1
            loss_check += 1

    if goal == 1000:
        print("Player won the amount")
    elif stake == 0:
        print("Player Lost")
    else:
        print("Enter correct stake or goal")


Gambling_Game(100, 1000)