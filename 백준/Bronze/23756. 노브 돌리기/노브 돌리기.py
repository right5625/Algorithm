N = int(input())
A = int(input())
result = 0
for i in [int(input()) for _ in range(N)]:
    result += min(abs(i - A), 360 - abs(i - A))
    A = i
print(result)