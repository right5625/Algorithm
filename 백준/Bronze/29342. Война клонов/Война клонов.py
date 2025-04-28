n = int(input())
N = [0, 0]
for i in list(map(int, input().split())):
    N[i % 2] += 1
print(N[0] * N[1])