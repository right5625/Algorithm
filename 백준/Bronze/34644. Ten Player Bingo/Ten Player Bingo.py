A = list(map(int, input().split()))
print(A[-1] % 10 if A[-1] % 10 != 0 else 10)