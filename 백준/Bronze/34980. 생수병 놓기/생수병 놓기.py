input()
S1 = input()
S2 = input()
if S1.count('w') > S2.count('w'):
    print('Oryang')
elif S1.count('w') < S2.count('w'):
    print('Manners maketh man')
else:
    print('Its fine' if S1 != S2 else 'Good')