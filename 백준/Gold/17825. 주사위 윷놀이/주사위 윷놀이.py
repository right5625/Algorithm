graph = {'0': ['2'], '2': ['4'], '4': ['6'], '6': ['8'], '8': ['10b'],
         '10b': ['12', '13b'], '12': ['14'], '14': ['16'], '16': ['18'], '18': ['20b'],
         '13b': ['16b'], '16b': ['19b'], '19b': ['25'],
         '20b': ['22', '22b'], '22': ['24'], '24': ['26'], '26': ['28'], '28': ['30b'],
         '22b': ['24b'], '24b': ['25'],
         '30b': ['32', '28b'], '32': ['34'], '34': ['36'], '36': ['38'], '38': ['40'],
         '28b': ['27b'], '27b': ['26b'], '26b': ['25'],
         '25': ['30'], '30': ['35'], '35': ['40'], '40': ['End']
         }

# horse = {i: [] for i in ['0', '2', '4', '6', '8', '10b', '12', '14', '16', '18', '13b', '16b', '19b', '20b', '22', '24', '26', '28', '22b', '24b', '30b', '32', '34', '36', '38', '28b', '27b', '26b', '25', '30', '35', '40']}
# horse['0'] = [0, 1, 2, 3]

from copy import deepcopy

def play(pos, score, cnt):
    if cnt == 10:
        global result
        result = max(result, score)
        return

    newPos = deepcopy(pos)
    for i in range(4):
        if newPos[i] == 'End':
            continue

        if newPos[i][-1] == 'b' and len(graph[newPos[i]]) == 2:
            cur = graph[newPos[i]][1]
        else:
            cur = graph[newPos[i]][0]

        for _ in range(A[cnt] - 1):
            if cur == 'End':
                break
            cur = graph[cur][0]

        newPos[i] = cur

    for i in range(4):
        if newPos[i] == 'End':
            pos[i], newPos[i] = newPos[i], pos[i]
            play(pos, score, cnt + 1)
            pos[i], newPos[i] = newPos[i], pos[i]
        elif newPos[i] in pos:
            continue
        else:
            pos[i], newPos[i] = newPos[i], pos[i]
            play(pos, score + int(pos[i][:-1] if pos[i][-1] == 'b' else pos[i]), cnt + 1)
            pos[i], newPos[i] = newPos[i], pos[i]

A = list(map(int, input().split()))
result = 0
play(['0'] * 4,  0, 0)
print(result)