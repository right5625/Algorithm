import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    z = int(input())
    if z == 0:
        break
    z3 = z ** 3
    max_sum = 0
    for x in range(1, z):
        x3 = x ** 3
        if x3 >= z3:
            break
        for y in range(1, z):
            s = x3 + y ** 3
            if s <= z3:
                if s > max_sum:
                    max_sum = s
            else:
                break
    print(z3 - max_sum)