N = int(input())
last, result = 0, []
for i in list(map(int, input().split())):
    if last < i:
        result.append(i)
        last = i
print(len(result))
print(*result)