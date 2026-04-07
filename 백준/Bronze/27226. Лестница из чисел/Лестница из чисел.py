a = int(input())
b = int(input())
k = int(input())
for i in range(a, b + 1):
    start = (i - 1) * i // 2 + 1
    length = min(i, k)
    row = []
    for j in range(length):
        row.append(start + j)
    print(*row)