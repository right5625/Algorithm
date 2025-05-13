S = input()
T = input()
print(''.join(i for i in T if i not in set(S)))