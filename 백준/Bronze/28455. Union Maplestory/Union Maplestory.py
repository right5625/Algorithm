N = int(input())
result = [0, 0]
for i in sorted([int(input()) for _ in range(N)], reverse=True)[:42]:
    result[0] += i
    if i >= 250:
        result[1] += 5
    elif i >= 200:
        result[1] += 4
    elif i >= 140:
        result[1] += 3
    elif i >= 100:
        result[1] += 2
    elif i >= 60:
        result[1] += 1
print(*result)