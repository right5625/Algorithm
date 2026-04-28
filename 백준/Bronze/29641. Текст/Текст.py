k = int(input())
cur, cnt = [], 0
for i in input().split():
    if len(cur) + cnt + len(i) <= k:
        cur.append(i)
        cnt += len(i)
    else:
        print(*cur)
        cur = [i]
        cnt = len(i)
if cur:
    print(*cur)