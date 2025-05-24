# 순열
N = int(input())
DP = [0] * 1000001
DP[2] = 1
for i in range(3, N + 1):
    DP[i] = (i - 1) * (DP[i - 2] + DP[i - 1]) % 1000000000
print(DP[N])