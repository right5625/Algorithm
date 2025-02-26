while True:
    n = int(input().strip())
    if n == -1:
        break
    dp = [[[[0] * 2 for _ in range(5)] for _ in range(16)] for _ in range(n + 1)]
    for h in range(1, 5):
        dp[1][1 << (h - 1)][h][0] = 1
    for i in range(1, n):
        for mask in range(16):
            for last in range(1, 5):
                for has_diff_3 in range(2):
                    if dp[i][mask][last][has_diff_3] == 0:
                        continue
                    for new_h in range(1, 5):
                        new_mask = mask | (1 << (new_h - 1))
                        new_has_diff_3 = has_diff_3 or (abs(last - new_h) == 3)
                        dp[i + 1][new_mask][new_h][new_has_diff_3] += dp[i][mask][last][has_diff_3]
    res = 0
    for mask in range(16):
        if bin(mask).count('1') >= 3:
            res += sum(dp[n][mask][last][1] for last in range(1, 5))
    print(f'{n}: {res}')