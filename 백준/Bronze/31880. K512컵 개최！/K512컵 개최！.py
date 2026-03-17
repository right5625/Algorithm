N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
P = sum(a)
for i in b:
    if i:
        P *= i
print(P)