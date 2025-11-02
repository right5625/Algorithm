for case in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    result = 'YES'
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if A[j] - A[i] == A[k] - A[j]:
                    result = 'NO'
    print(f'Case #{case + 1}: {result}')