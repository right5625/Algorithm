G = int(input())
N = int(input())
X = [0] * N
wins = []
for i in range(N):
    X[i] = int(input())
    cur = []
    for _ in range(X[i]):
        cur.append(int(input()))
    wins.append(cur)
result1 = 0
for j in range(X[0]):
    if wins[0][j] == 1:
        result1 += 1
result2 = 0
for i in range(N):
    a = 0
    b = 0
    for j in range(X[i]):
        if wins[i][j] == 1:
            a += 1
        else:
            b += 1
        if a >= G:
            break
        if b >= G:
            result2 += 1
            break
result3 = 1
maxA = -1
for G1 in range(1, G):
    A = 0
    for i in range(N):
        a = 0
        b = 0
        for j in range(X[i]):
            if wins[i][j] == 1:
                a += 1
            else:
                b += 1

            if a >= G1:
                A += 1
                break
            if b >= G1:
                break
    if maxA < A:
        maxA = A
        result3 = G1
print(f'{result1}\n{result2}\n{result3}')