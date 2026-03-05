import sys
input = lambda: sys.stdin.readline().rstrip()

lst = [input() for _ in range(int(input()))]
s = input()
result = []
for i in lst:
    if len(i) == len(s):
        flag = False
        for j in range(len(i)):
            if s[j] != '*' and i[j] != s[j]:
                flag = True
                break
        if not flag:
            result.append(i)
print(len(result))
print(*result, sep='\n')