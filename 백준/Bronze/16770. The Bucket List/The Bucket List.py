result = [0] * 1001
for _ in range(int(input())):
    s, t, b = map(int, input().split())
    for i in range(s, t + 1):
        result[i] += b
print(max(result))