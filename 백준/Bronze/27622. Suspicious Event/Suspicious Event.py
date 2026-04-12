input()
cur = set()
result = 0
for i in list(map(int, input().split())):
    if i > 0:
        cur.add(i)
    else:
        if abs(i) not in cur:
            result += 1
        else:
            cur.remove(abs(i))
print(result)