res = -1
for _ in range(int(input())):
    M, O = map(int, input().split())
    if O == 0:
        res = min(res, M) if res != -1 else M
print(res)