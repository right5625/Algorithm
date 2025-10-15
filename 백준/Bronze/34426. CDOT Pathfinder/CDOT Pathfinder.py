for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    result = M = 0
    for i in range(0, N * 2, 2):
        if M < A[i] / A[i + 1]:
            M = A[i] / A[i + 1]
            result = i // 2 + 1
    print(result)