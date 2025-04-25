result = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = (x * x + y * y) ** 0.5
    if d <= 10:
        result += 10
    elif d <= 30:
        result += 9
    elif d <= 50:
        result += 8
    elif d <= 70:
        result += 7
    elif d <= 90:
        result += 6
    elif d <= 110:
        result += 5
    elif d <= 130:
        result += 4
    elif d <= 150:
        result += 3
    elif d <= 170:
        result += 2
    elif d <= 190:
        result += 1
print(result)