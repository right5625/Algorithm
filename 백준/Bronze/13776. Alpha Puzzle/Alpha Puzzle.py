res = ''
for _ in range(int(input())):
    for i in input():
        if i != ' ' and i not in res:
            res += i
print(res)