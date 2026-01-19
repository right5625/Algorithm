N = int(input())
A = list(map(int, input().split()))
mx, mn = max(A), min(A)
for i in range(N):
    print(max(abs(A[i] - mx), abs(A[i] - mn)))