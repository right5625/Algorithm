n = int(input())
arr = [0] + list(map(int, input().split()))
odd_count = 0
even_count = 0
for i in range(1, n + 1):
    if i % 2 == 0 and arr[i] % 2 == 1:
        odd_count += 1
    if i % 2 == 1 and arr[i] % 2 == 0:
        even_count += 1
result = []
if odd_count == 1 and even_count == 1:
    for i in range(1, n + 1):
        if i % 2 == 0 and arr[i] % 2 == 1:
            result.append(i)
        if i % 2 == 1 and arr[i] % 2 == 0:
            result.append(i)
    print(result[0], result[1])
elif n >= 3 and odd_count + even_count == 0:
    print(1, 3)
else:
    print(-1, -1)