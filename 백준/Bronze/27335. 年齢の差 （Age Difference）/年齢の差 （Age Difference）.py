N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    print(max(abs(A[i] - max(A)), abs(A[i] - min(A))))