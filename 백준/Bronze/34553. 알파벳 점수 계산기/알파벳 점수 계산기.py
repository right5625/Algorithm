S = input()
cur = result = 1
for i in range(1, len(S)):
    if S[i - 1] < S[i]:
        cur += 1
    else:
        cur = 1
    result += cur
print(result)