input()
A = list(map(int, input().split()))
print(f'{sum(A[:A.index(max(A))])}\n{sum(A[A.index(max(A)) + 1:])}')