a, b, c = map(int, input().split())
result = 0
for i in range(c + 1):
    for j in range(i + 1):
        if a + j > b + (i - j):
            result += 1
print(result)