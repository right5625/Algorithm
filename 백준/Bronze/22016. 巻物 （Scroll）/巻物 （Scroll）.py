N, K = map(int, input().split())
S = input()
print(S[:K - 1] + ''.join(S[i].upper() if S[i].islower() else S[i].lower() for i in range(K - 1, N)))