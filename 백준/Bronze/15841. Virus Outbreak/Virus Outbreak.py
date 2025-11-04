DP = [1] * 491
for i in range(3, 491):
    DP[i] = DP[i - 1] + DP[i - 2]
while True:
    n = int(input())
    if n == -1:
        break
    print(f'Hour {n}: {DP[n]} cow(s) affected')