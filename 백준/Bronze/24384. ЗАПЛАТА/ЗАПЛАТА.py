k = int(input())
n = left = right = 1
while True:
    if left <= k <= right:
        print(str(n ** 3)[k - left])
        break
    n += 1
    left = right + 1
    right = left + len(str(n ** 3)) - 1