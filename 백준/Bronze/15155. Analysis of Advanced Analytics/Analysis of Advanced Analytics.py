n, k = map(int, input().split())
cur, cnt = 0, 1
for i in list(map(int, input().split())):
    if cur + i <= k:
        cur += i
    else:
        cur = i
        cnt += 1
print(cnt)