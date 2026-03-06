a, b, c = map(int, input().split())
result = float('inf')
for i in '+-*/':
    n = a
    if i == '+':
        n += b
    elif i == '-':
        n -= b
    elif i == '*':
        n *= b
    elif i == '/' and n % b == 0:
        n //= b
    else:
        continue
    for j in '+-*/':
        if j == '+' and n + c >= 0:
            result = min(result, n + c)
        elif j == '-' and n - c >= 0:
            result = min(result, n - c)
        elif j == '*' and n * c >= 0:
            result = min(result, n * c)
        elif j == '/' and n % c == 0 and n // c >= 0:
            result = min(result, n // c)
print(result)