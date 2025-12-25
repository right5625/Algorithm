N = int(input())
A = list(map(int, input().split()))
print(1 if A == sorted(A) and len(set(A)) == N else 0)