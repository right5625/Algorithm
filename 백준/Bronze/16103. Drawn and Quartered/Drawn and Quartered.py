N, K = map(int, input().split())
S = input()
for _ in range(K % 3):
    S = S[:N // 4] + S[N // 4 * 3:] + S[N // 4:N // 4 * 3]
print(S)