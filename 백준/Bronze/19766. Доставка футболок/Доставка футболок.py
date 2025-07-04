n, k, t = map(int, input().split())
z = list(map(int, input().split()))
s = list(map(int, input().split()))
result = 0
for i in range(n):
    result += z[i]
    if result + k >= s[i]:
        result = max(result, s[i]) + t
    else:
        result += k
print(result)