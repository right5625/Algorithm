S, P = map(int, input().split())
result = [-1]
for i in range(1, P // 2):
    if S % i == 0 and S // i * 2 + i * 2 == P:
        result = [S // i, i]
        break
print(*result)