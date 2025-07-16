N = int(input())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
result = 0
for i in range(N):
    result += (h[i] + h[i + 1]) * w[i] / 2
print(result)