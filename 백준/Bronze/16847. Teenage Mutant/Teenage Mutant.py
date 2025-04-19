for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    S1 = input()
    check = [False] * k
    for _ in range(n):
        S2 = input()
        for i in range(k):
            if S1[i] == S2[i]:
                check[i] = True
    print(f'Data Set {t}:\n{check.count(False)}/{k}\n')