for _ in range(int(input())):
    N, S = map(int, input().split())
    print('Yes' if 10 ** 7 + N == S else 'No')