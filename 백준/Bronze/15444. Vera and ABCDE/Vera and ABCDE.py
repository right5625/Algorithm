dic = {'A': ['***', '*.*', '***', '*.*', '*.*'], 'B': ['***', '*.*', '***', '*.*', '***'], 'C': ['***', '*..', '*..', '*..', '***'], 'D': ['***', '*.*', '*.*', '*.*', '***'], 'E': ['***', '*..', '***', '*..', '***']}
input()
S = input()
res = [[dic[j][i] for j in S] for i in range(5)]
for i in range(5):
    print(''.join(res[i]))