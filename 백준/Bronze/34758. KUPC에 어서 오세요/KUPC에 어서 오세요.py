X, Y = map(int, input().split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(0 if X == x or Y == y else 1)