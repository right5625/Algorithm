scale = 'ABCDEFG'
while True:
    S = input()
    if S == '#':
        break
    res = 'That music is beautiful.'
    for i in range(len(S) - 1):
        idx = scale.index(S[i])
        if S[i + 1] not in [scale[(idx + 2) % 7], scale[(idx + 4) % 7], scale[(idx + 6) % 7]]:
            res = 'Ouch! That hurts my ears.'
            break
    print(res)