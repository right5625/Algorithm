for t in range(1, int(input()) + 1):
    D, N = map(int, input().split())
    if N == 1:
        K, S = map(int, input().split())
        result = D / ((D - K) / S)
    else:
        K1, S1 = map(int, input().split())
        K2, S2 = map(int, input().split())
        result = D / max((D - K1) / S1, (D - K2) / S2)
    print(f'Case #{t}: {result}')