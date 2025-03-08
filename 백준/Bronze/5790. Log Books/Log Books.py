while True:
    N = int(input())
    if N == 0:
        break
    res = 'PASS'
    tot = night = 0
    for _ in range(N):
        s1, e1, s2, e2 = map(lambda x: int(x[:2]) * 60 + int(x[3:]), input().split())
        if e2 - s2 > 120:
            res = 'NON'
        if s2 < s1:
            night += min(e2, s1) - s2
        if e2 > e1:
            night += e2 - max(s2, e1)
        tot += e2 - s2
    if tot < 3000 or night < 600:
        res = 'NON'
    print(res)