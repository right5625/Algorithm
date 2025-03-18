for t in range(1, int(input()) + 1):
    S = input()
    I, J = map(int, input().split())
    print(f"Case #{t}: {(S.count('B') * (J // len(S)) + S[:J % len(S)].count('B')) - (S.count('B') * ((I - 1) // len(S)) + S[:(I - 1) % len(S)].count('B'))}")