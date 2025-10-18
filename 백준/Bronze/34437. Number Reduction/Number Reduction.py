N = int(input())
result = 0
while N > 1:
    if N % 2 == 0:
        N //= 2
    else:
        N += N * 2 + 1
    result += 1
print(result)