def queen(r):
    if r == N:
        global result
        result += 1
        return
    for c in range(N):
        if c not in col and r + c not in diag1 and r - c not in diag2:
            col.add(c)
            diag1.add(r + c)
            diag2.add(r - c)
            queen(r + 1)
            col.remove(c)
            diag1.remove(r + c)
            diag2.remove(r - c)

N = int(input())
result = 0
col = set()
diag1 = set()
diag2 = set()
queen(0)
print(result)