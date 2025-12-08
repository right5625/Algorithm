N, M, T = map(int, input().split())
result = [True] * (T + 1)
for i in list(map(int, input().split())):
    for j in range(M):
        if i - j >= 0:
            result[i - j] = False
        if i + j + 1 <= T:
            result[i + j + 1] = False
print(result[1:].count(True))