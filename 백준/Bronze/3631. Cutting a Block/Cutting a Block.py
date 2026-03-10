x, y, z, n = map(int, input().split())
for i in range(n):
    print(f'{x / n * i:.8f} 0.0 0.0 {x / n * (i + 1):.8f} {float(y):.8f} {float(z):.8f}')