n, m = map(int, input().split())
ctp = [list(map(int, input().split())) for _ in range(n)]
d = list(map(int, input().split()))
min_cost, result = float('inf'), 1
for i, (c, t, p) in enumerate(ctp, 1):
    total = c * 100 + sum(((v + t - 1) // t) * p for v in d if v >= t)
    if total < min_cost:
        min_cost = total
        result = i
print(result)