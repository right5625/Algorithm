M = list(map(int, input().split()))
result = 0
for _ in range(int(input())):
    B, L, S = input().split()
    if float(L) >= 2.0 and int(S) >= 17:
        result += M[int(B)]
print(result)