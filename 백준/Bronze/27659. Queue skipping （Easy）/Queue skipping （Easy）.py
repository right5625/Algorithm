for _ in range(int(input())):
    input()
    n, e = map(int, input().split())
    lst = [i for i in range(1, n + 1)]
    for _ in range(e):
        lst = [lst.pop(lst.index(int(input())))] + lst
    print(lst[-1])