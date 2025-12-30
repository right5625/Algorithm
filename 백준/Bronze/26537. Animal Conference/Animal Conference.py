for _ in range(int(input())):
    z = int(input())
    A = sorted([list(map(int, input().split())) for _ in range(z)])
    dist = float('inf')
    result = []
    for i in range(z - 1):
        for j in range(i + 1, z):
            cur = ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5
            if dist > cur:
                dist = cur
                result.clear()
                result.append([A[i][0], A[i][1], A[j][0], A[j][1]])
            elif dist == cur:
                result.append([A[i][0], A[i][1], A[j][0], A[j][1]])
    print(*sorted(result)[0])