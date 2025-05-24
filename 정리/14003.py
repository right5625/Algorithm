# DP
N = int(input())
A = [0] + list(map(int, input().split()))
idx = 0
ml = 1
B = [0] * (N + 1)
D = [0] * (N + 1)
res = [0] * (N + 1)
B[1] = A[1]
D[1] = 1
for i in range(2, N + 1):
    if B[ml] < A[i]:
        ml += 1
        B[ml] = A[i]
        D[i] = ml
    else:
        l = 1
        r = ml
        while l < r:
            mid = (l + r) // 2
            if B[mid] < A[i]:
                l = mid + 1
            else:
                r = mid
        idx = l
        B[idx] = A[i]
        D[i] = idx
print(ml)
idx = ml
for i in range(N, 0, -1):
    if D[i] == idx:
        res[idx] = A[i]
        idx -= 1
print(*res[1 : ml + 1])