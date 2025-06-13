from copy import deepcopy

board = {'0': ['2'], '2': ['4'], '4': ['6'], '6': ['8'], '8': ['10b'], '10b': ['12', '13b'], '12': ['14'], '14': ['16'], '16': ['18'], '18': ['20b'], '13b': ['16b'], '16b': ['19b'], '19b': ['25'], '20b': ['22', '22b'], '22': ['24'], '24': ['26'], '26': ['28'], '28': ['30b'], '22b': ['24b'], '24b': ['25'], '30b': ['32', '28b'], '32': ['34'], '34': ['36'], '36': ['38'], '38': ['40'], '28b': ['27b'], '27b': ['26b'], '26b': ['25'], '25': ['30'], '30': ['35'], '35': ['40'], '40': ['end']}
def play(cur_pos_horses, score, turn):
    if turn == 10:
        global result
        result = max(result, score)
        return
    next_pos_horses = deepcopy(cur_pos_horses)
    for i in range(4):
        if cur_pos_horses[i] == 'end':
            continue
        if cur_pos_horses[i][-1] == 'b' and len(board[cur_pos_horses[i]]) == 2:
            cur = board[cur_pos_horses[i]][1]
        else:
            cur = board[cur_pos_horses[i]][0]
        for _ in range(dice[turn] - 1):
            if cur == 'end':
                break
            cur = board[cur][0]
        next_pos_horses[i] = cur
        if cur == 'end':
            play(next_pos_horses, score, turn + 1)
        elif cur not in cur_pos_horses:
            play(next_pos_horses, score + int(next_pos_horses[i][:-1] if next_pos_horses[i][-1] == 'b' else next_pos_horses[i]), turn + 1)
        next_pos_horses[i] = cur_pos_horses[i]

dice = list(map(int, input().split()))
result = 0
play(['0'] * 4,  0, 0)
print(result)