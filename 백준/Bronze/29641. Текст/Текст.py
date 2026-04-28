k = int(input())
s = input().split()
cur = ''
for i in s:
    if not cur:
        cur += i
    elif len(cur + i) + 1 <= k:
        cur += ' ' + i
    else:
        print(cur)
        cur = i
if cur:
    print(cur)