# 2 players nim game with 2 sequence /wins the one that can't remove any nucleotides according to the rule below
# in every round the player removes 2 from one sequence and 1 from the other
# player 1 plays with winning strategy
# player 2 plays randomly
import random
import numpy as np
from matplotlib import pyplot as plt

sequenceA = []  # contains nucleotide sequence1
sequenceB = []  # contains nucleotide sequence2

PLOT_RESULT = 1  # plot whole game 0/1


def convert_data_to_list(seq, filename):
    file = open('data/'+str(filename))
    f_data = file.read()
    split_data = f_data.splitlines()  # splitlines to remove white spaces and \n chars
    data_len = len(split_data)  # number of sub sequences
    for i in range(1, data_len):  # ignore header
        seq.extend(list(split_data[i]))  # list every sub list


def player_1():  # player1 will choose a losing position if possible for his enemy
    move_1 = -1  # remove 2 nucleotides from sequence A and 1 from sequence B
    move_2 = -1  # remove 1 nucleotides from sequence A and 2 from sequence B
    if ((index_A - 2) % 3 == 0 or (index_A - 2) % 3 == 2) and index_A - 2 > index_B - 1:  # general row rule winning pos
        move_1 = 1
    elif ((index_A - 1) % 3 == 0 or (index_A - 1) % 3 == 2) and index_A - 1 > index_B - 2:
        move_2 = 1

    if (index_A - 2) % 3 == 1 and index_A - 2 > index_B - 1:  # general row rule losing position
        move_1 = 0
    elif (index_A - 1) % 3 == 1 and index_A - 1 > index_B - 2:
        move_2 = 0

    if ((index_B - 1) % 3 == 0 or (index_B - 1) % 3 == 2) and index_B - 1 > index_A - 2:  # general line rule winning pos
        move_1 = 1
    elif ((index_B - 2) % 3 == 0 or (index_B - 2) % 3 == 2) and index_B - 2 > index_A - 1:
        move_2 = 1

    if (index_B - 1) % 3 == 1 and index_B - 1 > index_A - 2:  # general line rule losing position
        move_1 = 0
    elif (index_B - 2) % 3 == 1 and index_B - 2 > index_A - 1:
        move_2 = 0

    if index_A - 2 == index_B - 1:  # diagonal rule
        if index_A % 3 == 2:
            move_1 = 0
        else:
            move_1 = 1
    elif index_A - 1 == index_B - 2:
        if index_A % 3 == 2:
            move_2 = 0
        else:
            move_2 = 1

    if ((index_A - 2) - (index_B - 1) == 1 or (index_A - 2) - (index_B - 1) == -1) or \
            ((index_A - 1) - (index_B - 2) == 1 or (index_A - 1) - (index_B - 2) == -1):
        if (index_A - 2) % 3 == 2 and (index_B - 1) % 3 == 0:  # upper lose out of 3x3
            move_1 = 0
        elif (index_A - 1) % 3 == 2 and (index_B - 2) % 3 == 0:
            move_2 = 0

        if (index_A - 2) % 3 == 0 and (index_B - 1) % 3 == 2:  # lower lose out of 3x3
            move_1 = 0
        elif (index_A - 1) % 3 == 0 and (index_B - 2) % 3 == 2:
            move_2 = 0

    # choose the best move
    if move_1 == 0:  # the goal is to make a move that sends the enemy to a losing position
        index_a = 2
        index_b = 1
    elif move_2 == 0:
        index_a = 1
        index_b = 2
    else:  # if next move leads in winning position for the enemy in both cases then pick randomly
        choice = random.uniform(0, 1)
        if choice > 0.5:
            index_a = 2
            index_b = 1
        else:
            index_a = 1
            index_b = 2
    return index_a, index_b


def player_2():
    choice = random.uniform(0, 1)  # pick a float between 0 and 1
    if choice > 0.5:  # give equal chances for the possible moves
        index_a = 2
        index_b = 1
    else:
        index_a = 1
        index_b = 2
    return index_a, index_b


convert_data_to_list(sequenceA, '6.14n.fasta')  # fill list sequenceA with file 6.14n.fast
convert_data_to_list(sequenceB, '6.14m.fasta')
n = len(sequenceA)
m = len(sequenceB)
index_A = n - 1
index_B = m - 1
data = np.array([n-1, m-1])

if (n < 2 and m < 2) or (n == 0 or m == 0):
    print('Always wins the first player, no move possible')
    quit()
elif (n == 1 and m >= 2) or (n >= 2 and m == 1):
    print('Always wins the second player')
    quit()

while True:
    if (index_A >= 2 and index_B >= 1) or (index_A >= 1 and index_B >= 2):
        move = player_1()
        index_A = index_A - move[0]
        index_B = index_B - move[1]
        data = np.vstack((data, (index_A, index_B)))
    else:
        print("Player 1 won")
        break
    if (index_A >= 2 and index_B >= 1) or (index_A >= 1 and index_B >= 2):
        move = player_2()
        index_A = index_A - move[0]
        index_B = index_B - move[1]
        data = np.vstack((data, (index_A, index_B)))
    else:
        print("Player 2 won")
        break

if PLOT_RESULT == 1:
    x, y = data.T
    plt.suptitle('Index of last nucleotide for both sequences after every move', fontsize=16)
    plt.xlabel('Nucleotide sequence A', fontsize=14)
    plt.ylabel('Nucleotide sequence B', fontsize=14)
    plt.plot(x, y, 'o-')
    plt.grid()
    plt.show()
else:
    quit()
