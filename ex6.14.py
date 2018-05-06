# 2 players nim game with 2 piles wins the one that can't pick nucleotides
# in every round the player chooses 2 from one pile and 1 from the other
# player 1 plays with winning strategy
# player 2 plays randomly
import random
import numpy as np

n = 100  # pile A size
m = 100  # pile B size
pileA = []*n
pileB = []*m
R = np.zeros((n, m))  # strategy array 1 means winning position 0 means losing position


def winning_strategy():
    R[1][1] = 1
    for i in range(n):  # pile b has 0 nucleotides so no move available
        R[i][0] = 1
    for j in range(m):  # pile a has 0 nucleotides so no move available
        R[0][j] = 1
    for i in range(2, n):  #
        R[i][1] = 0
    for j in range(2, m):
        R[1][j] = 0
    for i in range(2, n):
        for j in range(2, m):
            if R[i-2][j-1] == 1 and R[i-1][j-2] == 1:
                R[i][j] = 0
            else:
                R[i][j] = 1


def player_1():
    if R[i-2][j-1] == 0:
        # if this next move leads to losing position for enemy
        # pile a -2  pile b-1
        del pileA[i], pileA[i-1], pileB[i]
    elif R[i-1][j-2] == 0:
        # if this next move leads to losing position for enemy
        # pile a -1 pile b-1
        del pileA[i], pileB[i], pileB[i - 1]
    else:
        # if this move leads in winning position the enemy for both cases pick one
        choice = random.uniform(0, 1)
        if choice > 0.5:
            # remove 2 from pile a remove 1 from pile b
            del pileA[i], pileA[i - 1], pileB[i]
        else:
            # remove 1 from pile a remove 2 from pile b
            del pileA[i], pileB[i], pileB[i - 1]


def player_2():
    choice = random.uniform(0, 1)
    if choice > 0.5:
        print(choice)
        del pileA[i], pileA[i - 1], pileB[i]
        # remove 2 from pile a remove 1 from pile b
    else:
        print(choice)
        del pileA[i], pileB[i], pileB[i - 1]
        # remove 1 from pile a remove 2 from pile b


winning_strategy()
print(R)
