N = int(input())
S = input()
try:
    idx1 = S.index('I')
    idx2 = S[idx1:].index('O') + idx1
    idx3 = S[idx2:].index('I') + idx2
    print('Yes' if idx1 < idx2 < idx3 else 'No')
except:
    print('No')