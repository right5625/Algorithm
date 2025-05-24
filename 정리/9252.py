# DP
S1 = input()
S2 = input()
DP = [[0 for __ in range(len(S2) + 1)] for _ in range(len(S1) + 1)]
for i in range(1, len(S1) + 1):
    for j in range(1, len(S2) + 1):
        DP[i][j] = DP[i - 1][j - 1] + 1 if S1[i - 1] == S2[j - 1] else max(DP[i - 1][j], DP[i][j - 1])
print(DP[len(S1)][len(S2)])
if DP[len(S1)][len(S2)]:
    res = []
    i = len(S1)
    j = len(S2)
    while i != 0 and j != 0:
        if S1[i - 1] == S2[j - 1]:
            res.append(S1[i - 1])
            i -= 1
            j -= 1
        else:
            if DP[i - 1][j] > DP[i][j - 1]:
                i -= 1
            else:
                j -= 1
    res.reverse()
    print(*res, sep = '')