import sys
input = lambda: sys.stdin.readline().rstrip()

result = {'STU': 0, 'FAC': 0, 'VIS': 0}
for _ in range(int(input())):
    S = input().split()
    if S[1] == 'IN':
        result[S[0]] += int(S[2])
    else:
        result[S[0]] -= int(S[2])
print(sum(result.values()) if sum(result.values()) else 'NO STRAGGLERS')