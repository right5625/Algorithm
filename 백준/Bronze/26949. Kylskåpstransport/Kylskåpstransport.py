from math import ceil

pa, ka, pb, kb, n = map(int, input().split())
result = [0, 0, float('inf')]
for i in range(ceil(n / ka) + 1):
    if i * pa + ceil((n - (i * ka)) / kb) * pb < result[2]:
        result = [i, ceil((n - (i * ka)) / kb), i * pa + ceil((n - (i * ka)) / kb) * pb]
print(*result)