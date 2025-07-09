S = input()
if '-' in S:
    print('20' + ''.join(S.split('-')) if int(S[:2]) < 20 else '19' + ''.join(S.split('-')))
else:
    print('19' + ''.join(S.split('+')) if int(S[:2]) < 20 else '18' + ''.join(S.split('+')))