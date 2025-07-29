l = 'qwertasdfgzxcvb'
while True:
    S = input()
    if S == '#':
        break
    result = 0
    cur = True if S[0] in l else False
    for i in S[1:]:
        if (i not in l and cur) or (i in l and not cur):
            result += 1
            cur = not cur
    print(result)