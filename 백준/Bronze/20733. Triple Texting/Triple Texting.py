S = input()
words = [S[i:i + len(S) // 3] for i in range(0, len(S), len(S) // 3)]
for i in words:
    if words.count(i) > 1:
        print(i)
        break