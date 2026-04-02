n, m = map(int, input().split())
t = [int(input()) for _ in range(m)]
if sum(t) < n:
    print(*t, sep='\n')
else:
    result = [0] * m
    cur = cnt = 0
    while cnt < n:
        if t[cur]:
            t[cur] -= 1
            result[cur] += 1
            cnt += 1
        cur = (cur + 1) % m
    print(*result, sep='\n')