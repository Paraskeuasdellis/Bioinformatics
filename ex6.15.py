# 2 players nim game with 1 pile /wins the one that takes the last nucleotide
# in every round each player chooses either one or two from the pile
# player 1 plays with winning strategy
# player 2 plays randomly
import random
import numpy as np
from matplotlib import pyplot as plt

n = 88  # pile size
pile = [0]*n  # nucleotide pile
R = np.zeros(n)  # strategy array 1 indicates winning position 0 indicates losing position
data = np.array([n-1])


def winning_strategy():
    R[0], R[1], R[2] = 0, 1, 1  # if pile has 1 or 2 nucleotides left he wins /0 loses
    for i in range(3, n):
        if R[i-1] == 1 and R[i-2] == 1:
            R[i] = 0
        else:
            R[i] = 1


def player_1(i):
    index_move = 0  # it is equal to the nucleotides player will delete

    if R[i] == 1 and R[i-1] == 1:  # if current and next are winning pos delete 2 so opponent end up losing
        del pile[i], pile[i - 1]
        index_move = 2
    elif R[i] == 1 and R[i-1] == 0:  # if current pos is winning and next losing delete 1
        del pile[i]
        index_move = 1
    elif R[i] == 0:  # else pick randomly (like player2)
        choice = random.uniform(0, 1)
        if choice > 0.5:
            del pile[i]
            index_move = 1
        else:
            del pile[i], pile[i - 1]
            index_move = 2
    return index_move


def player_2(i):
    index_move = 0

    choice = random.uniform(0, 1)  # pick a float between 0 and 1
    if choice > 0.5:  # give equal chances for the possible moves
        del pile[i]
        index_move = 1
    else:
        del pile[i], pile[i-1]
        index_move = 2
    return index_move


winning_strategy()  # build strategy matrix

pile_index = n - 1  # create index that updates with every round /points at last nucleotide of the list

while True:
    move = player_1(pile_index)  # store the index_move
    pile_index = pile_index - move  # update index
    data = np.vstack((data, pile_index))
    if pile_index == 0:  # if no nucleotides left in the pile /means player did the last possible move
        print('Player 1 Won')
        break
    move = player_2(pile_index)
    pile_index = pile_index - move
    data = np.vstack((data, pile_index))
    if pile_index == 0:
        print('Player 2 Won')
        break


x = data.T
plt.suptitle('Index of last nucleotide of pile after every move', fontsize=16)
plt.xlabel('Pile', fontsize=14)
plt.plot(x, 0, 'o-', color='blue')
plt.grid()
plt.show()
