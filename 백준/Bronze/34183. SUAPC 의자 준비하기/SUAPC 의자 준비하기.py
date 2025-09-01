N, M, A, B = map(int, input().split())
print((N * 3 - M) * A + B if N * 3 - M > 0 else 0)