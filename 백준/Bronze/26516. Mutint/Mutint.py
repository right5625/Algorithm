while True:
    M = list(map(int, input()))
    if M == [0]:
        break
    M[M.index(max(M))] = 0 if max(M) % 2 == 1 else (M[M.index(max(M))] + 4) % 10
    print(int(''.join(list(map(str, M)))))