result = [0, float('inf'), 0, float('inf')]
for _ in range(int(input())):
    A = list(map(int, input().split()))[1:]
    result[0] = max(result[0], max(A))
    result[1] = min(result[1], min(A))
    result[2] = max(result[2], sum(A))
    result[3] = min(result[3], sum(A))
print(*result, sep='\n')