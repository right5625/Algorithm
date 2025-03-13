N, P, T = map(lambda x: int(x) if x.isdigit() else float(x), input().split())
SIM = [list(map(lambda x: int(x) if x.isdigit() else float(x), input().split())) for _ in range(N)]
res = [0] * N
res[0] = P
for i in range(1, T):
    s = cnt = 0
    for j in range(N):
        if i >= SIM[j][0] and res[j]:
            s += res[j]
            cnt += 1
    for j in range(N):
        if i >= SIM[j][0] and (i - SIM[j][0]) % SIM[j][1] == 0:
            res[j] = round(s / cnt * (1 + SIM[j][2]), 2)
for i in range(N):
    print(f'{res[i]:.2f}')