def calculate(g, gb, y, r, ry):
    S = g + gb + y + r + ry
    red = T // S * (r + ry)
    yellow = T // S * (y + ry)
    green = T // S * (g + gb // 2)
    rem = T % S
    time = 0
    if time + g <= rem:
        green += g
        time += g
    else:
        green += rem - time
        return red, yellow, green
    if time + gb <= rem:
        green += gb // 2
        time += gb
    else:
        green += (rem - time) // 2
        return red, yellow, green
    if time + y <= rem:
        yellow += y
        time += y
    else:
        yellow += rem - time
        return red, yellow, green
    if time + r <= rem:
        red += r
        time += r
    else:
        red += rem - time
        return red, yellow, green
    if time + ry <= rem:
        red += ry
        yellow += ry
        time += ry
    else:
        red += rem - time
        yellow += rem - time
    return red, yellow, green

g, gb, y, r, ry = map(int, input().split())
T = int(input())
print(*calculate(g, gb, y, r, ry))