import numpy as np

# 2 random DNA sequences
seq1 = ['.','T','G','C','G','G','C','A','T','G','G','C','C','C','T','A','T','T','A','G','C','T','A','A','A','G','G','C','A','T','G','C','C','T','T','A','A','A','A','G','T','C','G','T','G','A','A','T','C']
seq2 = ['.','G','G','C','A','G','C','T','A','G','T','C','C','C','A','A','G','T','T','C','C','A','A']
# Matrix to be filled with scores
score_matrix = np.zeros((len(seq2)+1,len(seq1)+1))
# 0= horizontal, 1 = vertical , 2 = diagonal
# list to help us traceback which keeps the horizontal-vertical-diagonal values for one element of the score_matrix
trace_back = [[0 for x in range(3)] for y in range(len(seq1)*len(seq2))]

# random match-missmatch values
dict = {'Match':1,'Missmatch': -1,'Gap':-2}

def fill_score_matrix():
    counter = 0
    # fill first row and column of the table according to the algorithm
    for i in range(len(seq1)+1):
        score_matrix[0][i] = dict['Gap'] * i
    for j in range(len(seq2)+1):
        score_matrix[j][0] = dict['Gap'] * j
    # fill rest of the table and save hor-vert-diag values for the tracebacking
    for i in range(len(seq2)):
        for j in range(len(seq1)):
            horizontal_score = score_matrix[i+1][j] + dict['Gap']
            vertical_score = score_matrix[i][j+1] + dict['Gap']
            if seq2[i] == seq1[j]:
                diagonal_score = score_matrix[i][j] + dict['Match']
            else:
                diagonal_score = score_matrix[i][j] + dict['Missmatch']
            trace_back[counter][0] = horizontal_score
            trace_back[counter][1] = vertical_score
            trace_back[counter][2] = diagonal_score
            maximum = max(horizontal_score,vertical_score,diagonal_score)
            score_matrix[i+1][j+1]= maximum
            counter+=1

def traceback():
    # initialization of values
    k = 0
    z = len(seq2)
    w = len(seq1)
    alignseq1 = ''
    alignseq2 = ''
    for i in range (max(len(seq1),len(seq2))):

        maxval = max(trace_back[(z-1)*len(seq1)+w-1])
        # Finding if maxval comes horizontally,vertically or diagonally for k<2
        if k<2:

            if maxval == trace_back[(z-1)*len(seq1)+w-1][0]  :
                alignseq1+= seq1[w-1]
                alignseq2+= '_'
                w = w-1
                k+= 1

            elif maxval == trace_back[(z-1)*len(seq1)+w-1][1]  :
                alignseq1+= '_'
                alignseq2+= seq2[z-1]
                z = z - 1
                k+=1
            # k = 0 if we insert at both sequences
            elif maxval == trace_back[(z-1)*len(seq1)+w-1][2] :
                alignseq1 += seq1[w-1]
                alignseq2 += seq2[z-1]

                z = z - 1
                w = w - 1
                k = 0
        # if k >= 2 we insert at both sequences and make k = 0
        else:
            alignseq1 += seq1[w - 1]
            alignseq2 += seq2[z - 1]

            z = z - 1
            w = w - 1
            k = 0


    print(alignseq1)
    print(alignseq2)

print('\n')
fill_score_matrix()
traceback()
print('\n')
print(score_matrix)


