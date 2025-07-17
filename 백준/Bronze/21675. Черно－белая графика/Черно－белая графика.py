w, h = map(int, input().split())
a = [input() for _ in range(h)]
b = [input() for _ in range(h)]
s = input()
for i in range(h):
    t = ''
    for j in range(w):
        if a[i][j] == '0':
            t += s[0] if b[i][j] == '0' else s[1]
        else:
            t += s[2] if b[i][j] == '0' else s[3]
    print(t)