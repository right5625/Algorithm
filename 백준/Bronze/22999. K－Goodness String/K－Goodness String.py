for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    S = input()
    score = 0
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            score += 1
    print(f'Case #{case}: {abs(K - score)}')