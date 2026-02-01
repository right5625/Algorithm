S = input()
for i, j in zip((-2, -2, -1, -1, 1, 1, 2, 2), (-1, 1, -2, 2, -2, 2, -1, 1)):
    if 'a' <= chr(ord(S[0]) + i) <= 'h' and 1 <= int(S[1]) + j <= 8:
        print(chr(ord(S[0]) + i) + str(int(S[1]) + j))