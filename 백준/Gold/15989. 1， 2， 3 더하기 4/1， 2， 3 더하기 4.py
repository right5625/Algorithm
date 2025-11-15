DP = [0] * 10001
DP[1], DP[2], DP[3] = 1, 2, 3
for i in range(4, 10001):
    DP[i] = DP[i - 3] + i // 2 + 1
for _ in range(int(input())):
    print(DP[int(input())])