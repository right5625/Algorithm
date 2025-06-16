minX, minY, maxX, maxY = 100, 100, 0, 0
for _ in range(int(input())):
    X, Y = map(int, input().split(','))
    minX = min(minX, X - 1)
    minY = min(minY, Y - 1)
    maxX = max(maxX, X + 1)
    maxY = max(maxY, Y + 1)
print(f'{minX},{minY}\n{maxX},{maxY}')