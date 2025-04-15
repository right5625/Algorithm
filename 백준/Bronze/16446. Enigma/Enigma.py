S1 = input()
S2 = input()
res = 0
for i in range(len(S1) - len(S2) + 1):
    T = S1[i:i + len(S2)]
    flag = True
    for j in range(len(S2)):
        if T[j] == S2[j]:
            flag = False
    if flag:
        res += 1
print(res)