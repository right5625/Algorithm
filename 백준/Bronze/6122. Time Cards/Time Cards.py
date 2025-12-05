N1, N2 = map(int, input().split())
start = {str(i): 0 for i in range(1, N1 + 1)}
result = {str(i): 0 for i in range(1, N1 + 1)}
for _ in range(N2):
    S = input().split()
    if S[1] == 'START':
        start[S[0]] = int(S[2]) * 60 + int(S[3])
    else:
        result[S[0]] += int(S[2]) * 60 + int(S[3]) - start[S[0]]
for i in range(1, N1 + 1):
    print(f'{result[str(i)] // 60} {result[str(i)] % 60}')