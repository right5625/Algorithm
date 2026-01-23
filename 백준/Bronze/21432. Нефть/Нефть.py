n, a, b = map(int, input().split())
result = 0
a_arr, b_arr = [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a_arr.append(ai)
    b_arr.append(bi)
    result = max(result, a / ai, b / bi)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        result = max(result, a / a_arr[i] + b / b_arr[j])
print(f'{result:.2f}')