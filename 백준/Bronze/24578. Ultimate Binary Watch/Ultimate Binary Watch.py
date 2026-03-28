N = list(map(int, input()))
div = 8
for _ in range(4):
    S = []
    for i in range(4):
        if N[i] // div:
            S.append('*')
            N[i] -= div
        else:
            S.append('.')
    print(' '.join(S[:2] + [' '] + S[2:]))
    div //= 2