while True:
    try:
        N = int(input())
        X = list(map(int, input().split()))
        result = 1
        if N > 2:
            for i in range(N - 2, 0, -1):
                if X[i] - X[i - 1] != X[N - 1] - X[N - 2]:
                    result = i + 1
                    break
        print(result)
    except:
        break