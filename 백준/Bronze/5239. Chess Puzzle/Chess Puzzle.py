for _ in range(int(input())):
    A = list(map(int, input().split()))
    R, C = set(), set()
    for i in range(1, A[0] * 2 + 1, 2):
        R.add(A[i])
        C.add(A[i + 1])
    print('SAFE' if len(R) == len(C) == A[0] else 'NOT SAFE')