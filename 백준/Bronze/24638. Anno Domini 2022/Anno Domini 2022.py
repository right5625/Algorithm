S1 = input().split()
S2 = input().split()
if S1[0] == S2[0] == 'AD':
    print(abs(int(S1[1]) - int(S2[1])))
elif S1[1] == S2[1] == 'BC':
    print(abs(int(S1[0]) - int(S2[0])))
elif S1[0] == 'AD':
    print(int(S1[1]) + int(S2[0]) - 1)
else:
    print(int(S1[0]) + int(S2[1]) - 1)