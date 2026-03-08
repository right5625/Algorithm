s = list(input().split())
for _ in range(int(input())):
    print(sorted(s[int(i)] for i in input())[-1])