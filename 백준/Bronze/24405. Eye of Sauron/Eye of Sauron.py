S = input()
print('correct' if S.index('(') == len(S) - S.index(')') - 1 else 'fix')