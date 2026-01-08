while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    minRate = float('inf')
    result = [0, 0]
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= m:
            if b / a < minRate or (b / a == minRate and result[0] < a):
                minRate = b / a
                result = [a, b]
    print('No suitable tickets offered' if result == [0, 0] else f'Buy {result[0]} tickets for ${result[1]}')