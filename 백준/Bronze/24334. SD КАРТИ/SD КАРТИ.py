from math import ceil

t = 0
for _ in range(int(input())):
    h, m = map(int, input().split())
    t += h * 60 + m
result = float('inf')
for i in range(t // 240 + 1):
    cur = i * 10.9
    if t - i * 240 > 240:
        cur += ceil((t - i * 240) / 180) * 9.15
        pass
    elif t - i * 240 > 180:
        cur += 10.9
    else:
        cur += 9.15
    result = min(result, cur)
print(f'{result:.2f}')