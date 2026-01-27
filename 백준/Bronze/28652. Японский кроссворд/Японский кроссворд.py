n, m = map(int, input().split())
a = [input() for _ in range(n)]
for i in a:
    lst = []
    for j in i.split('.'):
        if j:
            lst.append(len(j))
    lst = [len(lst)] + lst
    print(*lst)
print()
for i in list(zip(*a)):
    lst = []
    for j in ''.join(i).split('.'):
        if j:
            lst.append(len(j))
    lst = [len(lst)] + lst
    print(*lst)