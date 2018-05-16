from math import log
from numpy import zeros

# Transition matrix
trans_p = [[0.00, 0.50, 0.50, 0.00],
           [0.00, 0.50, 0.25, 0.25],
           [0.00, 0.25, 0.50, 0.25],
           [0.00, 0.00, 0.00, 0.00]]
# Emission matrix
emit_p = [[0, 0.50, 0.25, 0],
          [0, 0.25, 0.50, 0],
          [0, 0.25, 0.25, 0]]
states = ['D1', 'D2']
obs = '112122'
V = zeros((len(states), len(obs)), dtype=int)
bt = zeros((len(states), len(obs)), dtype=int)

for i in range(len(states)):
    V[i][0] = log(emit_p[int(obs[0]) - 1][i + 1], 2) + log(trans_p[0][i + 1], 2)
t = 1
for sym in obs[1:]:  # For each observation
    for i in range(len(states)):  # For each state
        max_m = [V[0][t - 1] + log(trans_p[1][i + 1], 2),
                 V[1][t - 1] + log(trans_p[2][i + 1], 2)]
        if max_m[0] > max_m[1]:
            V[i][t] = log(emit_p[int(sym) - 1][i + 1], 2) + max_m[0]
            # bt is filled with zeros by default so we don't have to make changes here
        elif max_m[0] < max_m[1]:
            V[i][t] = log(emit_p[int(sym) - 1][i + 1], 2) + max_m[1]
            bt[i][t] = 1
        else:
            V[i][t] = log(emit_p[int(sym) - 1][i + 1], 2) + max_m[0]
            bt[i][t] = 2
    t += 1

trace = ['']
if V[0][len(states)] > V[1][len(states)]:
    best_index = [0]
    trace[0] = states[0]
else:
    best_index = [1]
    trace[0] = states[1]

for i in range(bt.shape[1] - 1, 0, -1):
    for j in range(len(trace)):
        if bt[best_index[j], i] != 2:
            trace[j] = states[bt[best_index[j]][i]] + '-' + trace[j]
            best_index[j] = bt[best_index[j]][i]
        else:
            trace.append(trace[j])
            best_index.append(best_index[j])
            trace[j] = states[0] + '-' + trace[j]
            trace[j+1] = states[1] + '-' + trace[j+1]
            best_index[j] = bt[0][i - 1]
            best_index[j+1] = bt[1][i - 1]

print('Optimal paths:')
for i in trace:
    print('start-' + i + '-end')

if V[0][len(states)] > V[1][len(states)]:
    best_index = 0
else:
    best_index = 1
print('with score: ' + str(V[best_index][t - 1] + log(trans_p[best_index + 1][3], 2)))


