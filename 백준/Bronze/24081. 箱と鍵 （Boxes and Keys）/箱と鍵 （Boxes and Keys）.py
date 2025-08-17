input().split()
A = list(map(int, input().split()))
B = set(map(int, input().split()))
result = 0
for i in A:
    if i in B:
        result += 1
print(result)