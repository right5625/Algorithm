from decimal import Decimal

_, inc0, _, mul1, inc1 = input().split()
if Decimal(Decimal(inc0) * Decimal(mul1)).compare(Decimal(inc1)) == 1:
    print('Power up, Evolve')
elif Decimal(Decimal(inc0) * Decimal(mul1)).compare(Decimal(inc1)) == -1:
    print('Evolve, Power up')
else:
    print('Whatever')