N = int(input())
result = 0
while len(str(N)) == len(str(N * 2)):
    N *= 2
    result += 1
print(result)