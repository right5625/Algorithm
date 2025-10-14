n = int(input())
p = int(input())
print((set(i for i in range(p, n + p)) - set(map(int, input().split()))).pop())