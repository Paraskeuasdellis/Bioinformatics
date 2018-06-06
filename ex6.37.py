import random


def normal_sequence():
    seq = open('data/6.37.fasta').read()
    skip = 0
    new_seq = ''
    for i in range(len(seq)):
        if skip > 0:
            skip -= 1
            continue
        sub_seq = seq[i]
        for ii in range(i+1, len(seq)):
            if sub_seq[0] == seq[ii]:
                sub_seq += seq[ii]
                skip += 1
            else:
                break
        if sub_seq[0] == 'A':
            if len(sub_seq) % 6 == 0:
                new_seq += 'A'*(len(sub_seq) // 6)
            else:
                new_seq += 'A'*((len(sub_seq) // 6) + 1)
        elif sub_seq[0] == 'C':
            if len(sub_seq) % 11 == 0:
                new_seq += 'C' * (len(sub_seq) // 11)
            else:
                new_seq += 'C' * ((len(sub_seq) // 11) + 1)
        else:
            r = random.randint(6, 11)
            if len(sub_seq) % r == 0:
                new_seq += sub_seq[0] * (len(sub_seq) // r)
            else:
                new_seq += sub_seq[0] * ((len(sub_seq) // r) + 1)
    return new_seq


normal_seq = normal_sequence()
infected_seq = open('data/6.37.fasta').read()
offset = 0
inter_seq = ''
skip = 0
for i in range(len(normal_seq)):
    if skip > 0:
        skip -= 1
        continue
    sub_n = normal_seq[i]
    sub_i = ''
    for ii in range(i+1, len(normal_seq)):
        if sub_n[0] == normal_seq[ii]:
            sub_n += normal_seq[ii]
            skip += 1
        else:
            break
    for j in range(offset, len(infected_seq)):
        if sub_n[0] == infected_seq[j]:
            sub_i += infected_seq[j]
        else:
            break
    offset += len(sub_i)
    inter_seq += sub_i
    print(sub_n + ' -: ' + sub_i)
    print('...' + inter_seq[len(inter_seq)-min(18, len(inter_seq)):] + '|'
          + normal_seq[i+len(sub_n):i+len(sub_n)+18] + '...')
    print('-------------------------------')
