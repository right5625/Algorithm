N = int(input())
S = input()
result = 0
for i in range(N):
    if (i % 2 == 0 and S[i] != 'I') or (i % 2 == 1 and S[i] != 'O'):
        result += 1
print(result)