pt, p1, p2 = (int(round(i * 100, 1)) for i in map(float, input().split()))
i = 0
result = []
while p1 * i <= pt:
    if (pt - (p1 * i)) % p2 == 0:
        result.append([i, (pt - (p1 * i)) // p2])
    i += 1
if result:
    for i in result:
        print(*i)
else:
    print('none')