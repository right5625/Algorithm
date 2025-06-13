board = {'0': ['2'], '2': ['4'], '4': ['6'], '6': ['8'], '8': ['10b'], '10b': ['12', '13b'], '12': ['14'], '14': ['16'], '16': ['18'], '18': ['20b'], '13b': ['16b'], '16b': ['19b'], '19b': ['25'], '20b': ['22', '22b'], '22': ['24'], '24': ['26'], '26': ['28'], '28': ['30b'], '22b': ['24b'], '24b': ['25'], '30b': ['32', '28b'], '32': ['34'], '34': ['36'], '36': ['38'], '38': ['40'], '28b': ['27b'], '27b': ['26b'], '26b': ['25'], '25': ['30'], '30': ['35'], '35': ['40'], '40': ['end']}
def play(cur_pos_horses, score, turn):
    if turn == 10:
        global result
        result = max(result, score)
        return
    for i in range(4):
        if cur_pos_horses[i] == 'end':
            continue
        cur = board[cur_pos_horses[i]][1] if cur_pos_horses[i][-1] == 'b' and len(board[cur_pos_horses[i]]) == 2 else board[cur_pos_horses[i]][0]
        for _ in range(dice[turn] - 1):
            if cur == 'end':
                break
            cur = board[cur][0]
        if cur != 'end' and cur in cur_pos_horses:
            continue
        origin = cur_pos_horses[i]
        cur_pos_horses[i] = cur
        add_score = 0 if cur == 'end' else int(cur[:-1] if cur[-1] == 'b' else cur)
        play(cur_pos_horses, score + add_score, turn + 1)
        cur_pos_horses[i] = origin

dice = list(map(int, input().split()))
result = 0
play(['0'] * 4,  0, 0)
print(result)