N = int(input())
d = [150, 30, 15, 5, 1]
result = [0] * 5
idx = 0
while N:
    if N // d[idx]:
        result[idx] = N // d[idx]
        N %= d[idx]
    idx += 1
print(*result[::-1])