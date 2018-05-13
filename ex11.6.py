from math import log

# Transition matrix
trans_p = [[0.00, 0.50, 0.50, 0.00],
           [0.00, 0.50, 0.25, 0.25],
           [0.00, 0.25, 0.50, 0.25],
           [0.00, 0.00, 0.00, 0.00]]
# Emission matrix
emit_p = [[0, 0.50, 0.25, 0],
          [0, 0.25, 0.50, 0],
          [0, 0.25, 0.25, 0]]
obs = '112122'
V = [[0., 0.]]
k = 1
for sym in obs:  # For each observation
    V.append([])
    for i in range(2):  # For each state
        if V[k-1][0] > V[k-1][1]:
            V[k].append(log(emit_p[int(sym) - 1][i + 1], 2) + V[k - 1][0] + log(trans_p[1][i + 1], 2))
        elif V[k-1][0] == V[k-1][1] == 0:
            V[k].append(log(emit_p[int(sym) - 1][i + 1], 2) + V[k - 1][0] + log(trans_p[0][i + 1], 2))
        else:
            V[k].append(log(emit_p[int(sym) - 1][i + 1], 2) + V[k - 1][1] + log(trans_p[2][i + 1], 2))
    k += 1
trace1 = ''
trace2 = ''
for i in range(1, len(V)):
    if V[i][0] > V[i][1]:
        trace1 += 'D1-'
        trace2 += 'D1-'
    elif V[i][0] == V[i][1]:
        trace1 += 'D1-'
        trace2 += 'D2-'
    else:
        trace1 += 'D2-'
        trace2 += 'D2-'

print('start-' + trace1 + 'end')
print('start-' + trace2 + 'end')
