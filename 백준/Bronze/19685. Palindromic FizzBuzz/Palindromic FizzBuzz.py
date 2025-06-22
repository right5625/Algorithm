S, E = map(int, input().split())
for i in range(S, E + 1):
    print('Palindrome!' if str(i) == str(i)[::-1] else i)