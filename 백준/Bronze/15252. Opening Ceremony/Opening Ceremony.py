for t in range(1, int(input()) + 1):
    n, c = map(int, input().split())
    m = list(map(int, input().split()))
    for i in list(map(int, input().split())):
        m[i - 1] -= 1
    print(f'Data Set {t}:\n{max(m)}\n')