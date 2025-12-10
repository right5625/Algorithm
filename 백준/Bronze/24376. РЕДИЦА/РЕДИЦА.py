x, n = map(int, input().split())
left = right = cur = 1
while True:
    cur *= x
    left = right + 1
    right = left + len(str(cur)) - 1
    if left <= n <= right:
        print(str(cur)[n - left])
        break