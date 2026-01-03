lst = [[] for _ in range(9)]
for _ in range(int(input())):
    t, a, b = map(int, input().split())
    lst[a].append(t)
result = [0, 0]
for i in range(2):
    for j in range(1 + i * 4, 5 + i * 4):
        result[i] += 100 * len(lst[j])
        for k in range(len(lst[j]) - 1):
            if lst[j][k + 1] - lst[j][k] <= 10:
                result[i] += 50
print(*result)