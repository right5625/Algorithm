N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if A[i][i] != 0:
        print(1)
        exit()
for i in range(N):
    for j in range(N):
        if i != j and A[i][j] <= 0:
            print(2)
            exit()
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            print(3)
            exit()
for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i][j] + A[j][k] < A[i][k]:
                print(4)
                exit()
print(0)