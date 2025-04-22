N = int(input())
prevT, prevD = map(int, input().split())
result = 0
for _ in range(N - 1):
    t, d = map(int, input().split())
    result = max(result, (d - prevD) // (t - prevT))
    prevT, prevD = t, d
print(result)