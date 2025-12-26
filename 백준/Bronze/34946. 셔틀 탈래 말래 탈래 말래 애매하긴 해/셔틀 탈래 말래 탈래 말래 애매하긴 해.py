A, B, C, D = map(int, input().split())
if A + B <= D and C <= D:
    print('~.~')
elif A + B <= D:
    print('Shuttle')
elif C <= D:
    print('Walk')
else:
    print('T.T')