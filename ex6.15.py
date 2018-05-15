# 2 players nim game with 1 pile /wins the one that takes the last nucleotide
# in every round each player chooses either one or two from the pile
# player 1 plays with winning strategy
# player 2 plays randomly
import random
import numpy as np
from matplotlib import pyplot as plt

sequence = []  # contains nucleotide sequence
count = 0  # used to count the total moves


def convert_data_to_list():
    file = open('6.15-6.27.fasta')
    f_data = file.read()
    split_data = f_data.splitlines()  # splitlines to remove white spaces and \n chars
    data_len = len(split_data)  # number of sub sequences
    for i in range(1, data_len):  # ignore header
        sequence.extend(list(split_data[i]))  # list every sub list


def player_1():
    if index % 3 == 2:  # player is at winning position and needs to delete two nucleotide to send enemy to losing pos
        #del pile[index], pile[index - 1]
        index_move = 2
    elif index % 3 == 1:
        #del pile[index], pile[index - 1]
        index_move = 1
    elif index % 3 == 0:  # player is at losing position so he picks randomly
        choice = random.uniform(0, 1)
        if choice > 0.5:
            #del pile[index]
            index_move = 1
        else:
            #del pile[index], pile[index - 1]
            index_move = 2
    return index_move


def player_2():
    choice = random.uniform(0, 1)  # pick a float between 0 and 1
    if choice > 0.5:  # give equal chances for the possible moves
        #del pile[index]
        index_move = 1
    else:
        #del pile[index], pile[index - 1]
        index_move = 2
    return index_move


convert_data_to_list()
n = len(sequence)  # number of nucleotides
index = n - 1  # index to point at list after every round
data = np.array([n-1, count])


if index == 0:  # if there is only one nucleotide
    print('First player loses')
    quit()
if n == 0:  # if there are no nucleotides
    print('No one wins')
    quit()


while True:
    move = player_1()  # store the index_move
    count = count + 1  # update counter after each move
    index = index - move  # update index
    data = np.vstack((data, (index, count)))  # update array to plot
    if index == 0:  # if no nucleotides left in the pile /means player did the last possible move
        print('Player 1 Won')
        break
    move = player_2()
    count = count + 1
    index = index - move
    data = np.vstack((data, (index, count)))
    if index == 0:
        print('Player 2 Won')
        break

# plot the game
x, y = data.T
plt.suptitle('Index of last nucleotide of pile after every move', fontsize=16)
plt.xlabel('Nucleotide Sequence', fontsize=14)
plt.ylabel('Move', fontsize=14)
plt.plot(x, y, 'o-', color='blue')
plt.grid()
plt.show()
quit()
