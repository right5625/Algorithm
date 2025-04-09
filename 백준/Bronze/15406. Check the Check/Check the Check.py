tot = 0
while True:
    S = input()
    if S == 'TOTAL':
        print('PAY' if tot >= int(input()) else 'PROTEST')
        break
    p, c = map(int, input().split())
    tot += p * c