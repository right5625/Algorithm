N = int(input())
S = input()
result = float('inf')
for i in range(N - 4):
    cnt = 0
    for j, k in zip(S[i:i + 5], 'eagle'):
        if j != k:
            cnt += 1
    result = min(result, cnt)
print(result)