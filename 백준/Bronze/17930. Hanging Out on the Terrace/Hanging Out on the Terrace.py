L, x = map(int, input().split())
result = cur = 0
for _ in range(x):
    s, p = input().split()
    if s == 'enter':
        if cur + int(p) <= L:
            cur += int(p)
        else:
            result += 1
    else:
        cur -= int(p)
print(result)