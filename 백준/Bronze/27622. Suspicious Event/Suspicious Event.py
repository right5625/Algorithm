input()
cur = set()
result = 0
for i in list(map(int, input().split())):
    if i > 0:
        if i not in cur:
            cur.add(i)
        else:
            result += 1
    else:
        if abs(i) not in cur:
            result += 1
        else:
            cur.remove(abs(i))
print(result)