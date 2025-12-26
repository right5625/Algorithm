A, B, C, D = map(int, input().split())
if A + B <= D:
    print('~.~' if C <= D else 'Shuttle')
elif C <= D:
    print('Walk')
else:
    print('T.T')