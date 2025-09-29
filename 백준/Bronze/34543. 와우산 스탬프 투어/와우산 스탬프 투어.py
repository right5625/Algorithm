N = int(input())
W = int(input())
print(max(N * 10 + (20 if N >= 3 else 0) + (50 if N == 5 else 0)  - (15 if W > 1000 else 0), 0))