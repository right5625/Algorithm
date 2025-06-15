def queen(r):
    if r == N:
        global result
        result += 1
        return
    for c in range(N):
        if not col[c] and not diag1[r + c] and not diag2[r - c]:
            col[c] = True
            diag1[r + c] = True
            diag2[r - c] = True
            queen(r + 1)
            col[c] = False
            diag1[r + c] = False
            diag2[r - c] = False

N = int(input())
result = 0
col = [False] * N
diag1 = [False] * (N * 2)
diag2 = [False] * (N * 2)
queen(0)
print(result)