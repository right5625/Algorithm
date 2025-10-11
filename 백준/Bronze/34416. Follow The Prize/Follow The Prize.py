import sys
input = lambda: sys.stdin.readline().rstrip()

input()
result = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == result:
        result = b
    elif b == result:
        result = a
print(result)