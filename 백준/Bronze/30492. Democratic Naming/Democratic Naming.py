from collections import defaultdict

n, m = map(int, input().split())
lst = [defaultdict(int) for _ in range(m)]
for _ in range(n):
    s = input()
    for i in range(m):
        lst[i][s[i]] += 1
print(''.join(sorted(lst[i].items(), key=lambda x: (-x[1], x[0]))[0][0] for i in range(m)))