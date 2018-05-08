normal_seq = 'ATAGCTC'
infected_seq = 'AAATAAAGGGGCCCCCTTTTTTTCC'
offset = 0
inter_seq = ''
skip = False
for i in range(len(normal_seq)):
    if skip:
        skip = False
        continue
    sub_n = normal_seq[i]
    sub_i = ''
    for ii in range(i+1, len(normal_seq)):
        if sub_n[0] == normal_seq[ii]:
            sub_n += normal_seq[ii]
            skip = True
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
    print(inter_seq + normal_seq[i+1:])
    print('----------------')
