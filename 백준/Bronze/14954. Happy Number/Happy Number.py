n = int(input())
s = set()
s.add(n)
while True:
    n = sum(i * i for i in list(map(int, list(str(n)))))
    if n == 1:
        res = 'HAPPY'
        break
    elif n in s:
        res = 'UNHAPPY'
        break
    s.add(n)
print(res)