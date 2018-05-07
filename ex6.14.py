# 2 players nim game with 2 piles /wins the one that can't pick nucleotides according to the rule below
# in every round the player chooses 2 from one pile and 1 from the other
# player 1 plays with winning strategy
# player 2 plays randomly
import random
import numpy as np

n = 90  # pile A size
m = 90  # pile B size
pileA = [0]*n
pileB = [0]*m
R = np.zeros((n, m))  # strategy array 1 indicates winning position 0 indicates losing position


def winning_strategy():
    R[1][1] = 1
    for i in range(n):  # pile b has 0 nucleotides so no move available
        R[i][0] = 1
    for j in range(m):  # pile a has 0 nucleotides so no move available
        R[0][j] = 1
    for i in range(2, n):  # only one possible move that always leads to win for the enemy
        R[i][1] = 0
    for j in range(2, m):  # only one possible move that always leads to win for the enemy
        R[1][j] = 0
    for i in range(2, n):
        for j in range(2, m):
            if R[i-2][j-1] == 1 and R[i-1][j-2] == 1:  # if both possible moves lead to win pos for the enemy this is losing position
                R[i][j] = 0
            else:
                R[i][j] = 1


def player_1(i, j):
    index_a = 0  # it is equal to the nucleotides player will delete from each pile
    index_b = 0

    if R[i-2][j-1] == 0:  # if next move leads to losing position for enemy delete according movement
        del pileA[i], pileA[i-1], pileB[j]
        index_a = 2
        index_b = 1
    elif R[i-1][j-2] == 0:  # if next move leads to losing position for enemy delete according movement
        del pileA[i], pileB[j], pileB[j-1]
        index_a = 1
        index_b = 2
    else:
        choice = random.uniform(0, 1)  # if this move leads in winning position for the enemy in both cases the pick randomly
        if choice > 0.5:
            del pileA[i], pileA[i-1], pileB[j]
            index_a = 2
            index_b = 1
        else:
            del pileA[i], pileB[j], pileB[j - 1]
            index_a = 1
            index_b = 2
    return index_a, index_b


def player_2(i, j):
    index_a = 0
    index_b = 0

    choice = random.uniform(0, 1)  # pick a float between 0 and 1
    if choice > 0.5:  # give equal chances for the possible moves
        del pileA[i], pileA[i - 1], pileB[j]
        index_a = 2
        index_b = 1
    else:
        del pileA[i], pileB[j], pileB[j - 1]
        index_a = 1
        index_b = 2
    return index_a, index_b


winning_strategy()
# print(R)

index_pileA = n - 1
index_pileB = m - 1


while True:
    if (index_pileA >= 2 and index_pileB >= 1) or (index_pileA >= 1 and index_pileB >= 2):
        move = player_1(index_pileA, index_pileB)
        index_pileA = index_pileA - move[0]
        index_pileB = index_pileB - move[1]
    else:
        print("Player 1 won")
        break
    if (index_pileA >= 2 and index_pileB >= 1) or (index_pileA >= 1 and index_pileB >= 2):
        move = player_2(index_pileA, index_pileB)
        index_pileA = index_pileA - move[0]
        index_pileB = index_pileB - move[1]
    else:
        print("Player 2 won")
        break
# gia mikres stives an o player 1 ksekinaei apo losing pos uparxei pithanothta na xasei