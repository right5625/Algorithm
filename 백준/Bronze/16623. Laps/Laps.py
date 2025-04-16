n, m = map(int, input().split())
prev = res = 0
for i in list(map(int, input().split())):
    if prev > i:
        res += 1
    prev = i
print(res)