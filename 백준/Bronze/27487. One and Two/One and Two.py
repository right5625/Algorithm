for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    left = a[0]
    right = 1
    for i in a[1:]:
        right *= i
    if left == right:
        print(1)
    else:
        result = -1
        for i in range(1, n):
            left *= a[i]
            right //= a[i]
            if left == right:
                result = i + 1
                break
        print(result)