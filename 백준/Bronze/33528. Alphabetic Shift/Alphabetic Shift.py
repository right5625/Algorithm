S = list(input())
print(''.join(S))
for i in range(25):
    for j in range(len(S)):
        S[j] = chr(ord(S[j]) - 1 if ord(S[j]) - 1 >= ord('A') else ord(S[j]) + 25)
    print(''.join(S))