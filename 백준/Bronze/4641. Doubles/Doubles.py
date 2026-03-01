while True:
    A = sorted(list(map(int, input().split())))
    if A[0] == -1:
        break
    result, length = 0, len(A)
    for i in range(1, length - 1):
        for j in range(i + 1, length):
            if A[i] * 2 == A[j]:
                result += 1
    print(result)