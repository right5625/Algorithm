result = 0
for i, j in zip(sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())))):
    if i > j:
        result += 1
print(result)