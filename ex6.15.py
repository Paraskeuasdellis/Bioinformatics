# 2 players nim game with 1 pile wins the one that deletes the last nucleotide
# in every round the player chooses either one or two from the pile
# player 1 plays with winning strategy
# player 2 plays randomly
import random
import numpy as np

n = 100  # pile size
pile = []*n
R = np.zeros(n)


def winning_strategy():
    R[0], R[1], R[2] = 0, 1, 1
    for i in range(3, n):
        if R[i-1] == 1 and R[i-2] == 1:
            R[i] = 0
        else:
            R[i] = 1


def player_1(i):
    index_move = 0
    if R[i] == 1 and R[i-1] == 1:
        del pile[i], pile[i - 1]
        index_move = 2
    elif R[i] == 1 and R[i-1] == 0:
        del pile[i]
        index_move = 1
    elif R[i] == 0:
        choice = random.uniform(0, 1)
        if choice > 0.5:
            del pile[i]
            index_move = 1
        else:
            del pile[i], pile[i - 1]
            index_move = 2
    return index_move


def player_2(i):
    choice = random.uniform(0, 1)
    if choice > 0.5:
        del pile[i]
    else:
        del pile[i], pile[i-1]


winning_strategy()
i = n
while True:
    player_1(i)
    # afairw to index proxwraw tosa vhmata
    player_2(i)
    i = i - 1


print(R)
