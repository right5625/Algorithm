N, X = map(int, input().split())
A = list(map(int, input().split()))
tot = sum(A)
avg = tot / N
result = 0
while avg < X:
    tot += 100
    N += 1
    avg = tot / N
    result += 1
print(result)